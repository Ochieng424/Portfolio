from django.contrib import admin
from .models import MySkill


class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'rating', 'datestamp')


admin.site.register(MySkill, SkillAdmin)
