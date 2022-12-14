from django.contrib import admin

# Register your models here.

from .models import Book, UserProfile
from book_app.inlines import AuthorBookInline


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'type']
    ordering = ['-created_on']
    readonly_fields = ['name', 'location', 'type', 'birth_date']
    fieldsets = [
        (
            "General",
            {
                "fields": (
                    ("name",),
                    ("type",),
                    ("location",),
                    ("birth_date",),
                )
            },
        ),
    ]

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_inlines(self, request, obj):
        if obj and obj.type == "AUTHOR":
            return [AuthorBookInline]
        return []


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'edition']
    readonly_fields = ['name', 'price', 'edition', 'author', 'link']
    ordering = ['-created_on']

    def has_view_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
