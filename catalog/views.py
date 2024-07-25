from django.db.models import Q
from django.views import View
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Catalog, Category, Power as PowModel, Protection as ProModel, SubCategory


class CategoryListView(ListView):
    model = Category
    template_name = 'catalog/category_list.html'
    context_object_name = 'categories'
    slug_field = 'slug'
    slug_url_kwarg = 'category_slug'


class SubCategoryListView(ListView):
    model = SubCategory
    template_name = 'catalog/subcategory_list.html'
    context_object_name = 'subcategories'
    slug_field = 'slug'
    slug_url_kwarg = 'category_slug'

    def get_queryset(self):
        # Получаем подкатегории по slug категории
        category_slug = self.kwargs['category_slug']
        return SubCategory.objects.filter(category__slug=category_slug)

    def get_context_data(self, **kwargs):
        # Добавляем категорию в контекст
        context = super().get_context_data(**kwargs)
        category_slug = self.kwargs['category_slug']
        try:
            context['category'] = Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            context['category'] = None  # Или перенаправление на 404 страницу
        return context


class ProductListView(ListView):
    model = Catalog
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        # Получаем товары, связанные с подкатегорией
        return Catalog.objects.filter(subcategory_id=self.kwargs['subcategory_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем информацию о подкатегории в контекст
        context['subcategory'] = SubCategory.objects.get(id=self.kwargs['subcategory_id'])
        return context


class ProductDetailView(DetailView):
    model = Catalog
    template_name = 'catalog/product_detail.html'
    context_object_name = 'detail'
    slug_field = 'slug'  # Поле slug для поиска
    slug_url_kwarg = 'slug'  # Имя slug в URL



# class Category:
#
#     def get_category(self):
#         return CatModel.objects.all()
#
#     # def get_kelvin(self):
#     #     return KelModel.objects.all()
#
#     def get_protection(self):
#         return ProModel.objects.all()


# class CatalogView(Category, ListView):
#     model = Catalog
#     queryset = Catalog.objects.all()
#     template_name = 'catalog/catalog.html'
#     context_object_name = 'item_list'


# class CatalogDetailView(DetailView):
#     model = Catalog
#     slug_field = 'url'
#     context_object_name = 'detail'


# class Filters(Category, ListView):
#     template_name = 'catalog/catalog.html'
#     context_object_name = 'item_list'
#
#     def get_queryset(self, *args, **kwargs):
#         min_power = self.request.GET.get('min_power')
#         max_power = self.request.GET.get('max_power')
#
#         my_q = Q()
#         if 'category' in self.request.GET:
#             my_q = Q(category__url__in=self.request.GET.getlist('category'))
#         # if 'temp_sveta' in self.request.GET:
#         #     my_q &= Q(temp_sveta__url__in=self.request.GET.getlist('temp_sveta'))
#         if 'protection' in self.request.GET:
#             my_q &= Q(protection__url__in=self.request.GET.getlist('protection'))
#         if min_power:
#             my_q &= Q(power__gte=int(min_power))
#         if max_power:
#             my_q &= Q(power__lte=int(max_power))
#
#         queryset = Catalog.objects.filter(my_q)
#         return queryset
