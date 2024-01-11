from django.contrib import admin
from .models import Portfolio, Production, Slider


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'picture')


@admin.register(Production)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'picture')


@admin.register(Slider)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
