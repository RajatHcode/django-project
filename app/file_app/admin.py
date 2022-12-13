from django.contrib import admin

# Register your models here.

from file_app.models import FileUpload
admin.site.register(FileUpload)
