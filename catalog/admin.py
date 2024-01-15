from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Catalog, Category, CatalogImages


@admin.register(CatalogImages)
class CatalogImagesAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="80", height="80" ')

    get_image.short_description = 'Изображение'


class CatalogImagesInline(admin.TabularInline):
    model = CatalogImages
    extra = 1
    readonly_fields = ('get_image', )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="80", height="80" ')

    get_image.short_description = 'Изображение'


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('name',)}
    inlines = [CatalogImagesInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')


admin.site.site_title = 'ASV-LED'
admin.site.site_header = 'ASV-LED'

