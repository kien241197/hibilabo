from django.contrib import admin
from django.contrib.auth import get_user_model
from . import models, forms, utils
from django.http import HttpResponse
from django.shortcuts import render
from import_export.admin import ImportMixin
from django.contrib.auth.hashers import make_password
import json

# Register your models here.
CustomeUser = get_user_model()

admin.site.register(models.Company)
admin.site.register(models.Partner)
admin.site.register(models.Branch)
# admin.site.register(models.Hierarchy)
admin.site.register(models.HonneQuestion)
admin.site.register(models.SelfcheckQuestion)
admin.site.register(models.HonneEvaluationPeriod)
admin.site.register(models.SelfcheckEvaluationPeriod)

@admin.register(models.User)
class UsersAdmin(ImportMixin,admin.ModelAdmin):
    list_display = ("id","username")

    def import_action(self,request):
        import_object_status = []
        create_new_characters = []
        if request.method == "POST":
            # clear the list for every new request
            create_new_characters = []
            # capture payload from request
            csv_file = json.loads(request.POST.get("file_name"))
            reader = json.loads(request.POST.get("rows"))
            column_headers = json.loads(request.POST.get("csv_headers"))
            # helper class for validation and other stuff
            # look into git repo
            util_obj = utils.ImportUtils(column_headers)

            for row in reader:
                id = row[util_obj.get_column("id")]
                company_id = util_obj.validate_data(row[util_obj.get_column("company_id")])
                branch_id = util_obj.validate_data(row[util_obj.get_column("branch_id")])
                username = row[util_obj.get_column("username")]
                password = row[util_obj.get_column("password")]
                create_new_characters.append(
                    models.User(
                        id=id, company_id=company_id, branch_id=branch_id, username=username, password=password,
                    )
                )
                import_object_status.append({"username": username,"company_id": company_id,"branch_id": branch_id, "status": "FINISHED",
                                            "msg": "User created successfully!"})
            # bulk create objects
            # models.Characters.objects.bulk_create(create_new_characters)
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
                                    "[id,company_id,branch_id,username,password]."
                                    " The Following rows should contain information for the same.",
                                    "endpoint": "/admin/hibiLaboSystem/user/import/"}
        return render(
            request, "admin/import_users.html", context
        )