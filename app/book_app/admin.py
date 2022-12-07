from django.contrib import admin

# Register your models here.

from .models import Book, UserProfile
# admin.site.register(Book)
admin.site.register(UserProfile)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id']
    readonly_fields = ['author']
