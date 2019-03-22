from django.contrib import admin
from .models import Work


# Register your models here.
class WorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'datestamp')


admin.site.register(Work, WorkAdmin)
