from django.contrib import admin
from django.utils.safestring import mark_safe
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Catalog, Category, CatalogImages, Power, Protection, Kelvin, SubCategory


#
# @admin.register(CatalogImages)
# class CatalogImagesAdmin(admin.ModelAdmin):
#     list_display = ('title', 'get_image',)
#
#     def get_image(self, obj):
#         return mark_safe(f'<img src={obj.image.url} width="80", height="80" ')
#
#     get_image.short_description = 'Изображение'


class CatalogImagesInline(admin.TabularInline):
    model = CatalogImages
    extra = 1
    readonly_fields = ('get_image', )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100", height="100" ')

    get_image.short_description = 'Изображение'


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    inlines = [CatalogImagesInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'id')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'id')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Power)
class PowerAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'id')
    prepopulated_fields = {'url': ('name',)}


@admin.register(Kelvin)
class KelvinAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'id')
    prepopulated_fields = {'url': ('name',)}


@admin.register(Protection)
class ProtectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'id')
    prepopulated_fields = {'url': ('name',)}


admin.site.site_title = 'ASV-LED'
admin.site.site_header = 'ASV-LED'
# admin.site.register(Category, CategoryAdmin)

