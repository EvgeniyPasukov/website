from django.shortcuts import render
from .models import Catalog


def catalog_list(request):
    items = Catalog.objects.all()
    return render(request, 'catalog/catalog_list.html', {'items': items})


def details(request):
    return render(request, 'catalog/details.html')
