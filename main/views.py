from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def catalog(request):
    return render(request, 'catalog/catalog_list.html')


def portfolio(request):
    return render(request, 'main/portfolio.html')


def calc(request):
    return render(request, 'main/calc.html')


def contacts(request):
    return render(request, 'main/contacts.html')

