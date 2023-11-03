from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import *


class MenuItemMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20

    list_display = ('name', 'slug', 'parent')
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(MenuItem, MenuItemMPTTModelAdmin)
