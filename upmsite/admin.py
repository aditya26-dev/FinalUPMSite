from django.contrib import admin
from . import models

admin.site.site_header = "DJANGO ADMIN UPM SITE"
admin.site.register(models.Prodi)
admin.site.register(models.Folder)
admin.site.register(models.File)
admin.site.register(models.SubFolder01)
admin.site.register(models.SubFolder02)
admin.site.register(models.SubFile01)
admin.site.register(models.SubFile02)
# Register your models here.
