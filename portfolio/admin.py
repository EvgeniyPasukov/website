from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Portfolio, PortfolioImages


class PortfolioImagesInline(admin.TabularInline):
    model = PortfolioImages
    extra = 1
    readonly_fields = ('get_image', )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100", height="100" ')

    get_image.short_description = 'Изображение'


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'picture')
    prepopulated_fields = {'url': ('title',)}
    inlines = [PortfolioImagesInline]