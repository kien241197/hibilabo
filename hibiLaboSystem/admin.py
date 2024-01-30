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
    fields = ['username', 'first_name', 'last_name', 'email', 'role_id']
    extra = 0  # Number of empty forms to display
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

    def get_queryset(self, request):
        qs = super(UserInline, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(Q(created_by=request.user.id) | Q(company__created_by=request.user.id))
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
    exclude = ("created_by",)
    inlines = [WatasheetInline, MandaraPeriosInline, HonneEvaluationPeriodInline, SelfcheckEvaluationPeriodInline, BonknowEvaluationPeriodInline, UserInline]
    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user.id
        obj.save()

    def get_queryset(self, request):
        qs = super(CompanyAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(created_by=request.user.id)
        return qs
admin.site.register(Company, CompanyAdmin)
admin.site.register(Partner)
admin.site.register(Branch)


# admin.site.register(Hierarchy)

@admin.register(User)
class UsersAdmin(ImportMixin,admin.ModelAdmin):
    list_display = ("id","username")
    exclude = ('created_by','preferred_day','preferred_hour','preferred_day2','preferred_hour2','preferred_day3','preferred_hour3','preferred_day4','preferred_hour4','preferred_day5','preferred_hour5','preferred_day6','preferred_hour6','preferred_day7','preferred_hour7',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user.id
        obj.save()

    def get_form(self, request, obj=None, **kwargs):
        if not request.user.is_superuser:
            self.exclude = ("user_permissions", "is_superuser", "groups", "is_staff", "is_active",'created_by','preferred_day','preferred_hour','preferred_day2','preferred_hour2','preferred_day3','preferred_hour3','preferred_day4','preferred_hour4','preferred_day5','preferred_hour5','preferred_day6','preferred_hour6','preferred_day7','preferred_hour7',)
        form = super(UsersAdmin,self).get_form(request, obj, **kwargs)
        return form

    def get_field_queryset(self, db, db_field, request):
        if db_field.name == 'company' and not request.user.is_superuser:
            return db_field.remote_field.model._default_manager.filter(
                              Q(created_by=request.user.id)
            )

        super().get_field_queryset(db, db_field, request)

    def import_action(self,request):
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
            # helper class for validation and other stuff
            # look into git repo
            util_obj = utils.ImportUtils(column_headers)
            array_user = []
            for row in reader:
                username = row[util_obj.get_column("username")]
                first_name = row[util_obj.get_column("first_name")]
                last_name = row[util_obj.get_column("last_name")]
                password = row[util_obj.get_column("password")]
                if User.objects.filter(username=username).exists() or username in array_user:
                    import_object_status.append({"username": username, "status": "ERROR",
                                                "msg": "username already exist!"})
                else:
                    array_user.append(username)
                    try:
                        for validator in validators:
                            validator().validate(password)
                        create_new_characters.append(
                            User(
                                username=username, password=make_password(password), created_by=request.user.id, first_name=first_name, last_name=last_name
                            )
                        )
                        import_object_status.append({"username": username, "status": "FINISHED",
                                                    "msg": "User created successfully!"})
                    except ValidationError as e:
                        import_object_status.append({"username": username, "status": "ERROR",
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
        context = {"form": form, "form_title": "Upload users csv file.",
                    "description": "The file should have following headers: "
                                    "[username,password]."
                                    " The Following rows should contain information for the same.",
                                    "endpoint": "/admin/hibiLaboSystem/user/import/"}
        return render(
            request, "admin/import_users.html", context
        )
    def get_queryset(self, request):
        qs = super(UsersAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(is_superuser=False,created_by=request.user.id)
        return qs
# Honne
admin.site.register(HonneQuestion)
# Selfcheck
admin.site.register(SelfcheckQuestion)
# Bonknow
admin.site.register(ResponsQuestion)
admin.site.register(ThinkQuestion)
# Watasheet
admin.site.register(WatasheetQuestion)





