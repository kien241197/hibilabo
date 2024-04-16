from django.contrib import admin
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render
from import_export.admin import ImportMixin
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from . import forms, utils, validate
from django.forms import CheckboxSelectMultiple
from django.db import models
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.db.models import Q
import json
from django.core.cache import cache
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import redirect

import threading

thread_local = threading.local()


# Register your models here.
CustomeUser = get_user_model()
class HonneEvaluationPeriodInline(admin.TabularInline):
    model = HonneEvaluationPeriod
    extra = 0  # Number of empty forms to display
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
class SelfcheckEvaluationPeriodInline(admin.TabularInline):
    model = SelfcheckEvaluationPeriod
    extra = 0  # Number of empty forms to display
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
class BonknowEvaluationPeriodInline(admin.TabularInline):
    model = BonknowEvaluationPeriod
    extra = 0  # Number of empty forms to display
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
class UserInline(admin.TabularInline):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'role']
    extra = 0  # Number of empty forms to display
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

    def get_queryset(self, request):
        qs = super(UserInline, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(Q(created_by=request.user.id) | Q(company_id=request.user.company_id))
        return qs

class MandaraPeriosInline(admin.TabularInline):
    model = MandaraPeriod
    # fields = ['start_date', 'end_date', 'company_id']
    extra = 0  # Number of empty forms to display
    # formfield_overrides = {
    #     models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    # }

class WatasheetInline(admin.TabularInline):
    model = WatasheetEvaluationPeriod
    # fields = ['start_date', 'end_date', 'company_id']
    extra = 0  # Number of empty forms to display
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]
    exclude = ["created_by", "team_action_1_year", "team_action_5_years", "team_action_10_years", ]
    inlines = [HonneEvaluationPeriodInline, SelfcheckEvaluationPeriodInline, WatasheetInline, BonknowEvaluationPeriodInline, MandaraPeriosInline, UserInline]
    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user.id
        obj.save()

    def get_queryset(self, request):
        qs = super(CompanyAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(Q(created_by=request.user.id) | Q(id=request.user.company_id))
        return qs

    def get_form(self, request, obj=None, **kwargs):
        cache.clear()
        if not request.user.is_superuser:
            self.exclude = ["created_by", "team_action_1_year", "team_action_5_years", "team_action_10_years", "name", "date_start", "date_end", "active_flag", "partner"]
            self.inlines = []
        form = super(CompanyAdmin,self).get_form(request, obj, **kwargs)
        return form

class SelfcheckQuestionCustom(admin.ModelAdmin):
    list_filter = ["selfcheck_roles", "selfcheck_industries"]
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

class RoleCustom(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

# class SelfcheckIndustryCustom(admin.ModelAdmin):
#     filter_horizontal = ('Selfcheck_questions',)

@admin.register(User)
class UsersAdmin(ImportMixin,admin.ModelAdmin):
    list_display = ["id","username", "company", "branch", "role"]
    list_filter = ['company']
    exclude = ['created_by', 'password']
    actions = []
    success = True

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "branch":
            if request.user.is_superuser:
                kwargs["queryset"] = Branch.objects.all()
            else:
                if request.user.company_id:
                    kwargs["queryset"] = Branch.objects.filter(company_id=request.user.company_id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
   

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user.id
        
        if not request.user.is_superuser:
            obj.clean(current_user=request.user)
        
        obj.save()
               
    def get_form(self, request, obj=None, **kwargs):

        cache.clear()

        if not request.user.is_superuser:
            self.exclude = ["user_permissions", "is_superuser", "is_active",'created_by', 'password', 'company']
        form = super(UsersAdmin,self).get_form(request, obj, **kwargs)
        return form

    def get_field_queryset(self, db, db_field, request):
        if db_field.name == 'company' and not request.user.is_superuser:
            return db_field.remote_field.model._default_manager.filter(
                              Q(created_by=request.user.id) | Q(id=request.user.company_id)
            )

        super().get_field_queryset(db, db_field, request)

    def changelist_view(self, request, extra_context=None):
        cache.clear()
        if not request.user.is_superuser:
            self.list_display = ["id", "username", "branch"]
            self.actions = ['update_branch']
        return super(UsersAdmin, self).changelist_view(request, extra_context)

    def import_action(self,request):
        company_id = request.user.company_id
        role_id = Role.objects.filter(role=RoleEnum.Company_Staff.value).first().id
        import_object_status = []
        create_new_characters = []
        if request.method == "POST":
            validators = [validate.MinimumLengthValidator, validate.NumberValidator, validate.UppercaseValidator, validate.LowercaseValidator, validate.SymbolValidator]
            # clear the list for every new request
            create_new_characters = []
            # capture payload from request
            csv_file = json.loads(request.POST.get("file_name"))
            reader = json.loads(request.POST.get("rows"))
            
            column_headers = json.loads(request.POST.get("csv_headers"))
            format_column_headers = [row.replace('\r', '') for row in column_headers]
            
            # helper class for validation and other stuff
            # look into git repo
            util_obj = utils.ImportUtils(format_column_headers)
            array_user = []
            for row in reader:
                
                username = row[util_obj.get_column("username")]
                first_name = row[util_obj.get_column("first_name")]
                last_name = row[util_obj.get_column("last_name")] 
                password = row[util_obj.get_column("password")] 

                if request.user.is_superuser:
                    company_id = row[util_obj.get_column("company_id")] 
                else:
                    company_id = company_id

                branch_id = row[util_obj.get_column("branch_id")]

                if User.objects.filter(username=username).exists() or username in array_user:
                    import_object_status.append({"username": username, "company": company_id, "branch": branch_id, "status": "ERROR",
                                                "msg": "username already exist!"})
                                                
                elif Company.objects.filter(id=company_id).first() is None:
                    import_object_status.append({"username": username, "company": company_id, "branch": branch_id, "status": "ERROR",
                                            "msg": "company is not already exist!"}) 
                   

                elif Branch.objects.filter(id=branch_id ).first() is None:
                    import_object_status.append({"username": username, "company": company_id, "branch": branch_id, "status": "ERROR",
                                            "msg": "Branch is not already exist!"})
                   
                elif Company.objects.filter(id=company_id).first().id != Branch.objects.filter(id=branch_id).first().company.id:
                    import_object_status.append({"username": username, "company": company_id, "branch": branch_id, "status": "ERROR",
                                            "msg": "The branch must belong to the company!"})
                
                else:
                    array_user.append(username)
                    try:
                        for validator in validators:
                            validator().validate(password)
                        create_new_characters.append(
                            User(
                                username=username, password=make_password(password), created_by=request.user.id, first_name=first_name, last_name=last_name, company_id=company_id, branch_id=branch_id, role_id=role_id
                            )
                        )
                        if request.user.is_superuser:
                            import_object_status.append({"username": username, "company": company_id, "branch": branch_id,"status": "FINISHED",
                                                        "msg": "User created successfully!"})
                        else:
                            import_object_status.append({"username": username,"branch": branch_id, "status": "FINISHED",
                                                        "msg": "User created successfully!"})
                    except ValidationError as e:
                        import_object_status.append({"username": username, "company": company_id, "branch": branch_id, "status": "ERROR",
                                                "msg": str(e.args[0])})
                        
            # bulk create objects
            User.objects.bulk_create(create_new_characters)
            # return the response to the AJAX call
            context = {
                "file": csv_file,
                "entries": len(import_object_status),
                "results": import_object_status
            }
            return HttpResponse(json.dumps(context), content_type="application/json")
        # print(make_password('123456'));
        form = forms.CsvImportForm()
        if not request.user.is_superuser:
            context = {
                "form": form, 
                "form_title": "Upload users csv file.",
                "description": "The file should have following headers: "
                                "[username,first_name,last_name,password, branch_id]."
                                " The Following rows should contain information for the same.",
                                "endpoint": "/admin/hibiLaboSystem/user/import/",
            }
        else: 
            context = {
                "form": form, 
                "form_title": "Upload users csv file.",
                "description": "The file should have following headers: "
                                "[username,first_name,last_name,password, company_id, branch_id]."
                                " The Following rows should contain information for the same.",
                                "endpoint": "/admin/hibiLaboSystem/user/import/"
            }

        return render(
            request, "admin/import_users.html", context
        )
    def get_queryset(self, request):
        qs = super(UsersAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(Q(is_superuser=False) & (Q(created_by=request.user.id) | Q(company_id=request.user.company_id)))
        return qs

    def update_branch(self, request, queryset):
        if request.user.is_superuser:
            return HttpResponseRedirect(request.get_full_path())
            
        branches = Branch.objects.filter(company_id=request.user.company.id)
        if 'apply' in request.POST:
            queryset.update(branch_id=request.POST['branch'])
            
            self.message_user(request,
                              "ユーザー {} 人の支店が変更されました。".format(queryset.count()))
            return HttpResponseRedirect(request.get_full_path())
                        
        return render(request,
                      'admin/select_branch.html',
                      context={'users':queryset, 'branches': branches})

    update_branch.short_description = "新しい支店を選択"

class BranchAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'company']
    list_filter = ['company']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "company":
            if request.user.is_superuser is True:
                kwargs["queryset"] = Company.objects.all()
            else:
                if request.user.company_id:
                    kwargs["queryset"] = Company.objects.filter(id=request.user.company_id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def changelist_view(self, request, extra_context=None):
        cache.clear()
        if not request.user.is_superuser:
            self.list_display = ["id", "name"]
        return super(BranchAdmin, self).changelist_view(request, extra_context)

    def get_queryset(self, request):
        qs = super(BranchAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(company_id=request.user.company_id)
        return qs    


admin.site.register(Company, CompanyAdmin)
admin.site.register(Partner)
admin.site.register(Branch, BranchAdmin)
admin.site.register(Role, RoleCustom)
# Honne
admin.site.register(HonneQuestion)
# Selfcheck
admin.site.register(SelfcheckQuestion, SelfcheckQuestionCustom)
admin.site.register(SelfcheckRole)
# admin.site.register(SelfcheckIndustry, SelfcheckIndustryCustom)
# Bonknow
admin.site.register(ResponsQuestion)
admin.site.register(ThinkQuestion)
# Watasheet
admin.site.register(WatasheetQuestion)





