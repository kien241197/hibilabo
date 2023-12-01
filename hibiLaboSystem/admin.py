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
class CompanyAdmin(admin.ModelAdmin):
    inlines = [HonneEvaluationPeriodInline, SelfcheckEvaluationPeriodInline, BonknowEvaluationPeriodInline, UserInline]
admin.site.register(Company, CompanyAdmin)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_start', 'date_end', 'active_flag', 'partner', 'honne_evaluations')

    def person_name(self, obj):
        return obj.person.name if obj.person else '-'  # Replace 'name' with the actual field name in Person
    person_name.short_description = 'Person'
admin.site.register(Partner)
admin.site.register(Branch)
# admin.site.register(Hierarchy)

@admin.register(User)
class UsersAdmin(ImportMixin,UserAdmin):
    list_display = ("id","username")

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
                                username=username, password=make_password(password),
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
            return qs.filter(is_superuser=False)
        return qs
# Honne
admin.site.register(HonneQuestion)
# Selfcheck
admin.site.register(SelfcheckQuestion)
# Bonknow
admin.site.register(ResponsQuestion)
admin.site.register(ThinkQuestion)
