from django.contrib import admin
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin
from django.utils.html import format_html
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

from .models import *


# Hien thi Nhieu Truong thong tin tuy bien

# Import/Export du lieu;

# Register your models here.

class ContactContentResource(resources.ModelResource):
    class Meta:
        model = ContactContent


class ContactContentAdmin(ImportExportModelAdmin):
    resource_class = ContactContentResource
    list_display = (
        'name',
        'subject',
        'content',
        'updated_at',
        'created_at',
    )
    search_fields = (
        'name',
        'Subject',
    )
    readonly_fields = (
        'updated_at',
        'created_at',
    )

    class Media:
        js = ('BlogMgmt/admin/js/test.js',)
        css = {
            'all': ('BlogMgmt/admin/css/test.css',)
        }


admin.site.register(ContactContent, ContactContentAdmin)


class ContactPersonResource(resources.ModelResource):
    class Meta:
        model = ContactPerson


class ContactPersonAdmin(ImportExportModelAdmin):
    resource_class = ContactPersonResource
    list_display = (
        'name',
        'title',
        'email',
        'updated_at',
        'created_at',
    )
    search_fields = (
        'name',
        'title',
        'email',
    )
    readonly_fields = (
        'updated_at',
        'created_at',
    )

    class Media:
        js = ('BlogMgmt/admin/js/test.js',)
        css = {
            'all': ('BlogMgmt/admin/css/test.css',)
        }


admin.site.register(ContactPerson, ContactPersonAdmin)


class EmailTemplateResource(resources.ModelResource):
    class Meta:
        model = EmailTemplate


class EmailTemplateAdmin(ImportExportModelAdmin):
    resource_class = EmailTemplateResource
    list_display = (
        'name',
        'title',
        'updated_at',
        'created_at',
    )
    search_fields = (
        'name',
        'title',
    )
    readonly_fields = (
        'updated_at',
        'created_at',
    )

    class Media:
        js = ('BlogMgmt/admin/js/test.js',)
        css = {
            'all': ('BlogMgmt/admin/css/test.css',)
        }


admin.site.register(EmailTemplate, EmailTemplateAdmin)


class ContactMessageResource(resources.ModelResource):
    class Meta:
        model = ContactMessage


class ContactMessageAdmin(ImportExportModelAdmin):
    resource_class = ContactMessageResource
    list_display = (
        'name',
        'email',
        'updated_at',
        'created_at',
    )
    search_fields = (
        'name',
        'email',
    )
    readonly_fields = (
        'updated_at',
        'created_at',
    )

    class Media:
        js = ('BlogMgmt/admin/js/test.js',)
        css = {
            'all': ('BlogMgmt/admin/css/test.css',)
        }


admin.site.register(ContactMessage, ContactMessageAdmin)

