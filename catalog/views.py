from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Catalog


class CatalogView(ListView):
    model = Catalog
    queryset = Catalog.objects.all()
    template_name = 'catalog/catalog.html'
    context_object_name = 'item_list'


class CatalogDetailView(DetailView):
    model = Catalog
    slug_field = 'url'
    context_object_name = 'detail'
