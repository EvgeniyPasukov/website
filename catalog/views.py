from django.db.models import Q
from django.views.generic import ListView, DetailView
from .models import Catalog, Category as CatModel, Power as PowModel, Kelvin as KelModel, Protection as ProModel


class Category:

    def get_category(self):
        return CatModel.objects.all()

    def get_kelvin(self):
        return KelModel.objects.all()

    def get_protection(self):
        return ProModel.objects.all()


class CatalogView(Category, ListView):
    model = Catalog
    queryset = Catalog.objects.all()
    template_name = 'catalog/catalog.html'
    context_object_name = 'item_list'


class CatalogDetailView(DetailView):
    model = Catalog
    slug_field = 'url'
    context_object_name = 'detail'


class Filters(Category, ListView):
    template_name = 'catalog/catalog.html'
    context_object_name = 'item_list'

    def get_queryset(self, *args, **kwargs):
        min_power = self.request.GET.get('min_power')
        max_power = self.request.GET.get('max_power')

        my_q = Q()
        if 'category' in self.request.GET:
            my_q = Q(category__url__in=self.request.GET.getlist('category'))
        if 'temp_sveta' in self.request.GET:
            my_q &= Q(temp_sveta__url__in=self.request.GET.getlist('temp_sveta'))
        if 'protection' in self.request.GET:
            my_q &= Q(protection__url__in=self.request.GET.getlist('protection'))
        if min_power:
            my_q &= Q(power__gte=int(min_power))
        if max_power:
            my_q &= Q(power__lte=int(max_power))

        queryset = Catalog.objects.filter(my_q)
        return queryset
