from django.contrib import admin
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin
from django.utils.html import format_html

from .models import *

# Hien thi Nhieu Truong thong tin tuy bien

# Import/Export du lieu;

# Register your models here.

class LocationResource(resources.ModelResource):
    class Meta:
        model = Location

class LocationAdmin(ImportExportModelAdmin):
    resource_class = LocationResource
    list_display = (
        'name',
        'desc',
        # 'll_str',
        'desc_link',
        'updated_at',
        'created_at',
    )
    search_fields = (
        'name',
        'desc',
     )
    readonly_fields = (
        'updated_at',
        'created_at',
        'desc_link',
        # 'll_str',
    )
    class Media:
        js = ('BlogMgmt/admin/js/test.js',)
        css = {
             'all': ('BlogMgmt/admin/css/test.css',)
        }

    def desc_link(self, obj):
        return format_html(str('<a href="%s" target="_blank">%s</a>' % (obj.name, obj.updated_at)))
    desc_link.short_description = 'Desc Link'
    desc_link.allow_tags = True

admin.site.register(Location, LocationAdmin)

#######


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category

class CategoryAdmin(ImportExportModelAdmin):
    resource_class = CategoryResource
    list_display = (
        'name',
        'desc',
        # 'll_str',
        'desc_link',
        'updated_at',
        'created_at',
    )
    search_fields = (
        'name',
        'desc',
     )
    readonly_fields = (
        'updated_at',
        'created_at',
        'desc_link',
        # 'll_str',
    )
    class Media:
        js = ('BlogMgmt/admin/js/test.js',)
        css = {
             'all': ('BlogMgmt/admin/css/test.css',)
        }

    def desc_link(self, obj):
        return format_html(str('<a href="%s" target="_blank">%s</a>' % (obj.name, obj.updated_at)))
    desc_link.short_description = 'Desc Link'
    desc_link.allow_tags = True

admin.site.register(Category, CategoryAdmin)

#######


class StatusResource(resources.ModelResource):
    class Meta:
        model = Status

class StatusAdmin(ImportExportModelAdmin):
    resource_class = StatusResource
    list_display = (
        'name',
        'desc',
        # 'll_str',
        'desc_link',
        'updated_at',
        'created_at',
    )
    search_fields = (
        'name',
        'desc',
     )
    readonly_fields = (
        'updated_at',
        'created_at',
        'desc_link',
        # 'll_str',
    )
    class Media:
        js = ('BlogMgmt/admin/js/test.js',)
        css = {
             'all': ('BlogMgmt/admin/css/test.css',)
        }

    def desc_link(self, obj):
        return format_html(str('<a href="%s" target="_blank">%s</a>' % (obj.name, obj.updated_at)))
    desc_link.short_description = 'Desc Link'
    desc_link.allow_tags = True

admin.site.register(Status, StatusAdmin)

#######


class AuthorResource(resources.ModelResource):
    class Meta:
        model = Author

class AuthorAdmin(ImportExportModelAdmin):
    resource_class = AuthorResource
    list_display = (
        'name',
        'desc',
        # 'll_str',
        'desc_link',
        'updated_at',
        'created_at',
    )
    search_fields = (
        'name',
        'desc',
     )
    readonly_fields = (
        'updated_at',
        'created_at',
        'desc_link',
        # 'll_str',
    )
    class Media:
        js = ('BlogMgmt/admin/js/test.js',)
        css = {
             'all': ('BlogMgmt/admin/css/test.css',)
        }

    def desc_link(self, obj):
        return format_html(str('<a href="%s" target="_blank">%s</a>' % (obj.name, obj.updated_at)))
    desc_link.short_description = 'Desc Link'
    desc_link.allow_tags = True

admin.site.register(Author, AuthorAdmin)

#######


class PostResource(resources.ModelResource):
    class Meta:
        model = Post

class PostAdmin(ImportExportModelAdmin):
    resource_class = PostResource
    list_display = (
        'name',
        'desc',
        # 'll_str',
        'desc_link',
        'updated_at',
        'created_at',
    )
    search_fields = (
        'name',
        'desc',
     )
    readonly_fields = (
        'updated_at',
        'created_at',
        'desc_link',
        # 'll_str',
    )
    class Media:
        js = ('BlogMgmt/admin/js/test.js',)
        css = {
             'all': ('BlogMgmt/admin/css/test.css',)
        }

    def desc_link(self, obj):
        return format_html(str('<a href="%s" target="_blank">%s</a>' % (obj.name, obj.updated_at)))
    desc_link.short_description = 'Desc Link'
    desc_link.allow_tags = True

admin.site.register(Post, PostAdmin)

#######


class CommentPersonResource(resources.ModelResource):
    class Meta:
        model = CommentPerson

class CommentPersonAdmin(ImportExportModelAdmin):
    resource_class = CommentPersonResource
    list_display = (
        'name',
        'desc',
        # 'll_str',
        'desc_link',
        'updated_at',
        'created_at',
    )
    search_fields = (
        'name',
        'desc',
     )
    readonly_fields = (
        'updated_at',
        'created_at',
        'desc_link',
        # 'll_str',
    )
    class Media:
        js = ('BlogMgmt/admin/js/test.js',)
        css = {
             'all': ('BlogMgmt/admin/css/test.css',)
        }

    def desc_link(self, obj):
        return format_html(str('<a href="%s" target="_blank">%s</a>' % (obj.name, obj.updated_at)))
    desc_link.short_description = 'Desc Link'
    desc_link.allow_tags = True

admin.site.register(CommentPerson, CommentPersonAdmin)

#######


class CommentResource(resources.ModelResource):
    class Meta:
        model = Comment

class CommentAdmin(ImportExportModelAdmin):
    resource_class = CommentResource
    list_display = (
        'name',
        'desc',
        # 'll_str',
        'desc_link',
        'updated_at',
        'created_at',
    )
    search_fields = (
        'name',
        'desc',
     )
    readonly_fields = (
        'updated_at',
        'created_at',
        'desc_link',
        # 'll_str',
    )
    class Media:
        js = ('BlogMgmt/admin/js/test.js',)
        css = {
             'all': ('BlogMgmt/admin/css/test.css',)
        }

    def desc_link(self, obj):
        return format_html(str('<a href="%s" target="_blank">%s</a>' % (obj.name, obj.updated_at)))
    desc_link.short_description = 'Desc Link'
    desc_link.allow_tags = True

admin.site.register(Comment, CommentAdmin)

#######


class ReactionResource(resources.ModelResource):
    class Meta:
        model = Reaction

class ReactionAdmin(ImportExportModelAdmin):
    resource_class = ReactionResource
    list_display = (
        'name',
        'desc',
        # 'll_str',
        'desc_link',
        'updated_at',
        'created_at',
    )
    search_fields = (
        'name',
        'desc',
     )
    readonly_fields = (
        'updated_at',
        'created_at',
        'desc_link',
        # 'll_str',
    )
    class Media:
        js = ('BlogMgmt/admin/js/test.js',)
        css = {
             'all': ('BlogMgmt/admin/css/test.css',)
        }

    def desc_link(self, obj):
        return format_html(str('<a href="%s" target="_blank">%s</a>' % (obj.name, obj.updated_at)))
    desc_link.short_description = 'Desc Link'
    desc_link.allow_tags = True

admin.site.register(Reaction, ReactionAdmin)

#######
