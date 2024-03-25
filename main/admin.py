from django.contrib import admin
from .models import Slider


@admin.register(Slider)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

