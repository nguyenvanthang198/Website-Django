from django.contrib import admin
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin
from django.utils.html import format_html

from .models import *


# Register your models here.

class MenuResource(resources.ModelResource):
    class Meta:
        model = Menu


class MenuAdmin(ImportExportModelAdmin):
    resource_class = MenuResource
    list_display = (
        'admin_name',
        'title',
        'order',
        # 'desc',
        # 'll_str',
        # 'desc_link',
        'updated_at',
        'created_at',
    )
    search_fields = (
        'name',
        'title',
        # 'desc',
    )
    readonly_fields = (
        'updated_at',
        'created_at',
        'admin_name',
        # 'desc_link',
        # 'll_str',
    )
    #
    # class Media:
    #     js = ('BlogMgmt/admin/js/test.js',)
    #     css = {
    #         'all': ('BlogMgmt/admin/css/test.css',)
    #     }
    #
    # def desc_link(self, obj):
    #     return format_html(str('<a href="%s" target="_blank">%s</a>' % (obj.name, obj.updated_at)))
    #
    # desc_link.short_description = 'Desc Link'
    # desc_link.allow_tags = True


admin.site.register(Menu, MenuAdmin)

