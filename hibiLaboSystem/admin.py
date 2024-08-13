from django.contrib import admin
from django.contrib.auth import get_user_model
from django.http import HttpRequest, HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from import_export.admin import ImportMixin
from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ValidationError
from . import forms, utils, validate
from django.forms import CheckboxSelectMultiple, SelectMultiple, TextInput
from django.db import models
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.db.models import Q
import json
from django.core.cache import cache
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import redirect
import datetime
import threading
import jaconv
from django.utils.html import format_html
from django.contrib.auth.models import Group, Permission
from . import forms


thread_local = threading.local()

class MandaraBasePeriodInline(admin.TabularInline):
    model = MandaraBase
    fields = ["flg_finished"]

class ResponsResultPeriodInline(admin.TabularInline):
    model = ResponsResult
    fields = ["flg_finished"]

class WatasheetTypeResultPeriodInline(admin.TabularInline):
    model = WatasheetTypeResult
    fields = ["flg_finished"]

class HonneTypeResultPeriodInline(admin.TabularInline):
    model = HonneTypeResult
    fields = ["flg_finished"]

class SelfcheckTypeResultPeriodInline(admin.TabularInline):
    model = SelfcheckTypeResult
    fields = ["flg_finished"]

# Register your models here.
CustomeUser = get_user_model()

class HonneEvaluationPeriodInline(admin.TabularInline):
    model = HonneEvaluationPeriod
    fields = ["evaluation_name", "evaluation_start", "evaluation_end", "honne_questions"]
    extra = 0  # Number of empty forms to display
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
    readonly_fields=[]
        
    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser and request.user.role.role not in [RoleEnum.Company_Admin.value, RoleEnum.Partner.value, RoleEnum.Company_Director.value]:   
            self.readonly_fields = ["evaluation_name", "honne_questions"]
        return  self.readonly_fields
            
    # def get_queryset(self, request):
    #     qs = super(HonneEvaluationPeriodInline, self).get_queryset(request)
    #     if not request.user.is_superuser:
    #         today = datetime.date.today()
    #         return qs.filter(evaluation_start__lte=today, evaluation_end__gte=today)
    #     return qs


class SelfcheckEvaluationPeriodInline(admin.TabularInline):
    model = SelfcheckEvaluationPeriod
    fields = ["evaluation_name", "evaluation_start", "evaluation_end", "selfcheck_questions"]
    extra = 0  # Number of empty forms to display
    formfield_overrides = {
        models.ManyToManyField: {'widget': forms.CheckboxSelectMultipleWithSelectAll},
    }
    readonly_fields = []

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser and request.user.role.role not in [RoleEnum.Company_Admin.value, RoleEnum.Partner.value, RoleEnum.Company_Director.value]:
            self.readonly_fields = ["evaluation_name", "selfcheck_questions"]
        return self.readonly_fields
    
    # def get_queryset(self, request):
    #     qs = super(SelfcheckEvaluationPeriodInline, self).get_queryset(request)
    #     if not request.user.is_superuser:
    #         today = datetime.date.today()
    #         return qs.filter(evaluation_start__lte=today, evaluation_end__gte=today)
    #     return qs

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "selfcheck_questions" and len(request.resolver_match.kwargs.keys()) > 0:
            parent_obj_id = request.resolver_match.kwargs['object_id']
            company = Company.objects.get(pk=parent_obj_id)
            kwargs["queryset"] = SelfcheckQuestion.objects.filter(industries__in=[company.industry]).distinct()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
class BonknowEvaluationPeriodInline(admin.TabularInline):
    model = BonknowEvaluationPeriod
    fields = ["evaluation_name", "evaluation_start", "evaluation_end", "respons_questions", "think_questions"]
    extra = 0  # Number of empty forms to display
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
    readonly_fields = []

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser and int(request.user.role.role) not in [RoleEnum.Company_Admin.value, RoleEnum.Partner.value, RoleEnum.Company_Director.value]:
            self.readonly_fields = ["evaluation_name", "respons_questions", "think_questions"]
        return self.readonly_fields
        
    # def get_queryset(self, request):
    #     qs = super(BonknowEvaluationPeriodInline, self).get_queryset(request)
    #     if not request.user.is_superuser:
    #         today = datetime.date.today()
    #         return qs.filter(evaluation_start__lte=today, evaluation_end__gte=today)
    #     return qs
    
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
    extra = 0  # Number of empty forms to display
    
    # def get_queryset(self, request):
    #     qs = super(MandaraPeriosInline, self).get_queryset(request)
    #     if not request.user.is_superuser:
    #         today = datetime.date.today()
    #         return qs.filter(start_date__lte=today, end_date__gte=today)
    #     return qs 

class WatasheetInline(admin.TabularInline):
    model = WatasheetEvaluationPeriod
    fields = ["evaluation_name", "evaluation_start", "evaluation_end", "watasheet_questions"]
    extra = 0  # Number of empty forms to display
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
    readonly_fields = []

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser and request.user.role.role not in [RoleEnum.Company_Admin.value, RoleEnum.Partner.value, RoleEnum.Company_Director.value]:
            self.readonly_fields = ["evaluation_name", "watasheet_questions"]
        return self.readonly_fields

    # def get_queryset(self, request):
    #     qs = super(WatasheetInline, self).get_queryset(request)
    #     if not request.user.is_superuser:
    #         today = datetime.date.today()
    #         return qs.filter(evaluation_start__lte=today, evaluation_end__gte=today)
    #     return qs

class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]
    inlines = [HonneEvaluationPeriodInline, SelfcheckEvaluationPeriodInline, WatasheetInline, BonknowEvaluationPeriodInline, MandaraPeriosInline]
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
        self.exclude = ["created_by", "team_action_1_year", "team_action_5_years", "team_action_10_years"]
        if not request.user.is_superuser:
            self.exclude.extend(["name", "date_start", "date_end", "active_flag", "partner"])
            # self.inlines = []
            self.readonly_fields = ["industry"]
        form = super(CompanyAdmin,self).get_form(request, obj, **kwargs)
        return form

class SelfcheckQuestionCustom(admin.ModelAdmin):
    list_filter = ["selfcheck_roles", "industries"]
    search_fields = ["question"]
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

class ThinkQuestionCustom(admin.ModelAdmin):
    search_fields = ["question"]


class WatasheetQuestionCustom(admin.ModelAdmin):
    search_fields = ["question"]


class ResponsQuestionCustom(admin.ModelAdmin):
    search_fields = ["question"]


class HonneQuestionCustom(admin.ModelAdmin):
    search_fields = ["question"]

class RoleCustom(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }    

class IndustryCustom(admin.ModelAdmin):
    filter_horizontal = ('Selfcheck_questions',)

@admin.register(User)
class UsersAdmin(ImportMixin,admin.ModelAdmin):
    list_display = ["id","username", "company", "branch", "role"]
    list_filter = ['company',]
    inlines=[]
    actions = []
    
    success = True

    def has_import_permission(self, request):
        if not request.user.is_superuser and request.user.role.role not in [RoleEnum.日々研.value, RoleEnum.Partner.value, RoleEnum.Company_SuperVisor.value]:
            return False
        return True

    def add_view(self, request, form_url='', extra_context=None):
        response  = super().add_view(request, form_url, extra_context)
        if response.status_code == 302:
            user = User.objects.latest('id')
            if user.is_staff:
                groups = Group.objects.all()
                user.groups.set(groups)
            else:
                user.groups.set([])
            user.save()
        return response

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
            obj.password = make_password(obj.password)

        if not request.user.is_superuser:
            obj.company_id = request.user.company_id
            obj.add(request.user.company_id)

        obj.save()

        obj.groups.set([])
        obj.user_permissions.set([])
        if obj.role is not None:
            permissions_list = []
            if obj.role.role == RoleEnum.日々研.value:
                obj.is_superuser = True
            elif obj.role.role == RoleEnum.Partner.value:
                permissions_list = RolePermission.Partner.value
            elif obj.role.role == RoleEnum.Company_Admin.value:
                permissions_list = RolePermission.Company_Admin.value
            elif obj.role.role == RoleEnum.Company_Director.value:
                permissions_list = RolePermission.Company_Director.value
            elif obj.role.role == RoleEnum.Company_SuperVisor.value:
                permissions_list = RolePermission.Company_SuperVisor.value
            permissions = Permission.objects.filter(codename__in=permissions_list)
            obj.user_permissions.add(*permissions)

        obj.save()
               
    def get_form(self, request, obj=None, **kwargs):

        cache.clear()
        obj = obj.id if obj else False
        self.exclude = ['created_by', 'image', 'groups', "user_permissions", "is_superuser"]
        if obj:
            if not request.user.is_superuser:
                self.exclude = ["user_permissions", "is_superuser", "is_active",'created_by', 'company', 'password', 'groups', 'image']

        else:
            if not request.user.is_superuser:
                self.exclude = ["user_permissions", "is_superuser", "is_active",'created_by', 'company', 'groups', 'image' ]

        form = super(UsersAdmin,self).get_form(request, obj, **kwargs)
        return form

    def get_field_queryset(self, db, db_field, request):
        if db_field.name == 'company' and not request.user.is_superuser:
            return db_field.remote_field.model._default_manager.filter(
                              Q(created_by=request.user.id) | Q(id=request.user.company_id)
            )
        
        if db_field.name == 'role':
            if  not request.user.is_superuser:
                return db_field.remote_field.model._default_manager.exclude(
                                Q(role=90) | Q(role=40)
                )

        super().get_field_queryset(db, db_field, request)

    def changelist_view(self, request, extra_context=None):
        cache.clear()
        
        if not request.user.is_superuser:
            self.list_display = ["id", "username", "branch", "role"]
            self.actions = ['update_branch']
            self.inlines = [HonneTypeResultPeriodInline, SelfcheckTypeResultPeriodInline, WatasheetTypeResultPeriodInline, ResponsResultPeriodInline, MandaraBasePeriodInline]
        else:
            self.inlines = []
        return super(UsersAdmin, self).changelist_view(request, extra_context)

    def import_action(self,request):
        if not request.user.is_superuser and request.user.role.role not in [RoleEnum.日々研.value, RoleEnum.Partner.value, RoleEnum.Company_SuperVisor.value]:
            return HttpResponseForbidden()
        company_id = request.user.company_id
        role_id = Role.objects.filter(role=RoleEnum.Company_Staff.value).first().id
        import_object_status = []
        create_new_characters = []
        if request.method == "POST":
            try:
                validators = [validate.MinimumLengthValidator, validate.NumberValidator, validate.UppercaseValidator, validate.LowercaseValidator, validate.SymbolValidator]
                # clear the list for every new request
                create_new_characters = []
                # capture payload from request
                csv_file = json.loads(request.POST.get("file_name"))
                reader = json.loads(request.POST.get("rows"))
                
                column_headers = json.loads(request.POST.get("csv_headers"))
                format_column_headers = [row.replace('\r', '').strip() for row in column_headers]
                
                # helper class for validation and other stuff
                # look into git repo
                util_obj = utils.ImportUtils(format_column_headers)
                array_user = []

                users = list(User.objects.values_list('username', flat=True))
                if request.user.is_superuser:
                    companies = list(Company.objects.values_list('id', flat=True))
                    branches = list(Branch.objects.values_list('id', 'company_id', 'code'))
                else:
                    branches = list(Branch.objects.filter(company_id=company_id).values_list('id', 'company_id', 'code'))
                
                for row in reader:
                    username = row[util_obj.get_column("username")]
                    first_name = row[util_obj.get_column("first_name")]
                    last_name = row[util_obj.get_column("last_name")] 
                    password = row[util_obj.get_column("password")] 
                    branch_code = row[util_obj.get_column("branch_code")].replace('\r', '')

                    if request.user.is_superuser:
                        company_id = row[util_obj.get_column("company_id")]

                    branch_detail = []
                    if branch_code != '' and company_id != '':
                        branch_detail = [item for item in branches if int(item[1]) == int(company_id) and int(item[2]) == int(branch_code)]
                    if username == '':
                        import_object_status.append({"username": username, "company": company_id, "branch": branch_code, "status": "ERROR",
                                                    "msg": "Username is required!"})
                    elif company_id == '':
                        import_object_status.append({"username": username, "company": company_id, "branch": branch_code, "status": "ERROR",
                                                    "msg": "Company_id is required!"})
                    elif username in users:
                        import_object_status.append({"username": username, "company": company_id, "branch": branch_code, "status": "ERROR",
                                                    "msg": "Username already exist!"}) 
                        
                    elif request.user.is_superuser and int(company_id) not in companies:
                        import_object_status.append({"username": username, "company": company_id, "branch": branch_code, "status": "ERROR",
                                                "msg": "Company is not already exist!"})

                    elif branch_code != '' and len(branch_detail) == 0:
                        import_object_status.append({"username": username, "company": company_id, "branch": branch_code, "status": "ERROR",
                                                "msg": "Branch is not already exist!"})
                        
                    else:
                        brach_id = None
                        if len(branch_detail) > 0:
                            brach_id = branch_detail[0][0]

                        try:
                            for validator in validators:
                                validator().validate(password)
                            create_new_characters.append(
                                User(
                                    username=username, password=make_password(password), created_by=request.user.id, first_name=first_name, last_name=last_name, company_id=company_id, branch_id=brach_id, role_id=role_id
                                )
                            )
                            
                            import_object_status.append({"username": username, "company": company_id, "branch": branch_code,"status": "FINISHED",
                                                    "msg": "User created successfully!"})
                            users.append(username)
                            
                        except ValidationError as e:
                            import_object_status.append({"username": username, "company": company_id, "branch": branch_code, "status": "ERROR",
                                                    "msg": str(e.args[0])})
                User.objects.bulk_create(create_new_characters)

                context = {
                    "file": csv_file,
                    "entries": len(import_object_status),
                    "results": import_object_status
                }
                return HttpResponse(json.dumps(context), content_type="application/json")
                pass
            except Exception as e:
                return HttpResponse(e, content_type="application/json", status=500)
                raise e
        # print(make_password('123456'));
        form = forms.CsvImportForm()
   
        context = {
            "title": "インポート",
            "form": form, 
            "form_title": "Upload users csv file.",
            "description": "The file should have following headers: "
                            "[username,first_name,last_name,password,company_id,branch_code]."
                            " The Following rows should contain information for the same.",
            "endpoint": "/admin/hibiLaboSystem/user/import/",
            "is_nav_sidebar_enabled": self.admin_site.each_context(request).get("is_nav_sidebar_enabled"),
            "has_permission": self.admin_site.each_context(request).get("has_permission"),
            'available_apps': self.admin_site.each_context(request).get("available_apps")
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
                      context={
                        'users':queryset, 
                        'branches': branches,
                        "title": "新しい支店を選択",
                        "is_nav_sidebar_enabled": self.admin_site.each_context(request).get("is_nav_sidebar_enabled"),
                        "has_permission": self.admin_site.each_context(request).get("has_permission"),
                        'available_apps': self.admin_site.each_context(request).get("available_apps")
                        })

    update_branch.short_description = "新しい支店を選択"

class BranchAdmin(admin.ModelAdmin):
    list_filter = ['company']
    list_display = ['get_id_with_name', 'name', 'company']

    def get_id_with_name(self, obj):
        return f"{obj.company_id}_{obj.code}"
    get_id_with_name.allow_tags = True
    get_id_with_name.short_description = 'ID'

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "company":
            if request.user.is_superuser is True:
                kwargs["queryset"] = Company.objects.all()
            else:
                if request.user.company_id:
                    kwargs["queryset"] = Company.objects.filter(id=request.user.company_id)
                    kwargs["initial"] = request.user.company_id
                    kwargs["disabled"] = True
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def changelist_view(self, request, extra_context=None):
        cache.clear()
        if not request.user.is_superuser:
            self.list_display = ["get_id_with_name", "name"]
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
admin.site.register(HonneQuestion, HonneQuestionCustom)
# Selfcheck
admin.site.register(SelfcheckQuestion, SelfcheckQuestionCustom)
admin.site.register(SelfcheckRole)
admin.site.register(Industry, IndustryCustom)
# Bonknow
admin.site.register(ResponsQuestion, ResponsQuestionCustom)
admin.site.register(ThinkQuestion, ThinkQuestionCustom)
# Watasheet
admin.site.register(WatasheetQuestion, WatasheetQuestionCustom)
#Remove Group Permission
admin.site.unregister(Group)







