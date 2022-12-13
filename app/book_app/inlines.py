from django.contrib import admin
from book_app.models import Book


class AuthorBookInline(admin.TabularInline):
    model = Book
    readonly_fields = ['name', 'price', 'edition', 'link']
    fieldsets = (
        (None, {
            'fields': (("name"),
                       ("price", "edition"),
                       ("link",),)
        }
        ),
    )
    extra = 0

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
