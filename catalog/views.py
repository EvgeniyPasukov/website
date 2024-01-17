from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Catalog, Category as CatModel, Power as PowModel, Kelvin as KelModel, Protection as ProModel


class Category:
    '''категории товаров'''
    def get_category(self):
        return CatModel.objects.all()

    def get_kelvin(self):
        return Catalog.objects.all().values('temp_sveta')

    def get_protection(self):
        return ProModel.objects.all()


class Power:
    '''мощность товаров'''
    def get_power(self):
        return PowModel.objects.all()


class CatalogView(Category, ListView):
    model = Catalog
    queryset = Catalog.objects.all()
    template_name = 'catalog/catalog.html'
    context_object_name = 'item_list'


class CatalogDetailView(DetailView):
    model = Catalog
    slug_field = 'url'
    context_object_name = 'detail'


class FilterYearCategory(Category, ListView):
    template_name = 'catalog/catalog.html'
    context_object_name = 'item_list'

    def get_queryset(self):
        my_q = Q()
        if 'category' in self.request.GET:
            my_q = Q(category__in=self.request.GET.getlist('category'))
        if 'temp_sveta' in self.request.GET:
            my_q &= Q(temp_sveta__in=self.request.GET.getlist('temp_sveta'))
        if 'protection' in self.request.GET:
            my_q &= Q(protection__in=self.request.GET.getlist('protection'))

        queryset = Catalog.objects.filter(my_q)
        return queryset

