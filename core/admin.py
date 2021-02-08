from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Data


@admin.register(Data)
class PersonAdmin(ImportExportModelAdmin):
    pass
