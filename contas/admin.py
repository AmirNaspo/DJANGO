from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

admin.site.register(Categoria)
admin.site.register(empregado)
admin.site.register(Profile)
admin.site.register (Nutri)
admin.site.register (pont)