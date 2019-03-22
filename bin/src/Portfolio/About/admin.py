from django.contrib import admin

# Register your models here.

from .models import About


class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'featured')


admin.site.register(About, AboutAdmin)
