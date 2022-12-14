from django.contrib import admin

# Register your models here.

from file_app.models import FileUpload


@admin.register(FileUpload)
class FileUploadAdmin(admin.ModelAdmin):
    list_display = ['file', 'created_on']
    readonly_fields = ['file', 'created_on']
    ordering = ['-created_on']

    def has_view_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
