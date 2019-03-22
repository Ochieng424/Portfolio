from django.contrib import admin
from django.contrib.auth.models import Group

# Register your models here.
admin.site.site_header = 'Portfolio Admin'
admin.site.unregister(Group)
