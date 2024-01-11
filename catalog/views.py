from django.shortcuts import render
from django.views.generic.base import View

from .models import Catalog


# def catalog_list(request):
#     items = Catalog.objects.all()
#     return render(request, 'catalog/catalog.html', {'item_list': items})


class CatalogView(View):
    def get(self, request):
        items = Catalog.objects.all()
        return render(request, 'catalog/catalog.html', {'item_list': items})


class CatalogDetailView(View):
    def get(self, request, slug):
        detail = Catalog.objects.get(url=slug)
        return render(request, 'catalog/details.html', {'detail': detail})
