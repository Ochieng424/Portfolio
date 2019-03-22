from django.contrib import admin
from .models import Contact


# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('fullName', 'email', 'subject', 'message')
    list_display_links = None
    sortable_by = ('datestamp',)

    def has_add_permission(self, request):
        return False


admin.site.register(Contact, ContactAdmin)
