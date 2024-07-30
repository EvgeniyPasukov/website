from django.db.models import Q
from django.http import JsonResponse
from django.views import View
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.core.mail import send_mail
from django.conf import settings


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
    slug_url_kwarg = 'subcategory_slug'

    def get_queryset(self):
        # Получаем товары по slug подкатегории
        subcategory_slug = self.kwargs['subcategory_slug']
        return Catalog.objects.filter(subcategory__slug=subcategory_slug)

    def get_context_data(self, **kwargs):
        # Добавляем подкатегорию и категорию в контекст
        context = super().get_context_data(**kwargs)
        subcategory_slug = self.kwargs['subcategory_slug']

        try:
            context['subcategory'] = SubCategory.objects.get(slug=subcategory_slug)
            context['category'] = context['subcategory'].category
        except SubCategory.DoesNotExist:
            context['subcategory'] = None  # Или перенаправление на 404 страницу
            context['category'] = None

        return context


class ProductDetailView(DetailView):
    model = Catalog
    template_name = 'catalog/product_detail.html'
    context_object_name = 'detail'
    slug_field = 'slug'  # Поле slug для поиска
    slug_url_kwarg = 'product_slug'  # Имя slug в URL

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        url = request.POST.get('url')

        # Формируем сообщение
        subject = 'Запрос цены на светильник'
        message = (
            f'Имя: {name}.\n\n'
            f'email: {email}.\n\n'
            f'Телефон: {phone}.\n\n'
            f'Светильник: {url}\n\n'
        )
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = ['pasukov.e@yandex.ru']

        try:
            send_mail(
                subject,
                message,
                from_email,
                recipient_list,
                fail_silently=False # Если True, ошибки не будут выводиться
            )
            return JsonResponse({'message': 'Ваш запрос отправлен! Мы свяжемся с вами.'})
        except Exception as e:
            # Если произошла ошибка при отправке
            return JsonResponse({'error': f'Не удалось отправить запрос: {str(e)}'}, status=500)



# class Category:
#
#     def get_category(self):
#         return CatModel.objects.all()
#
#     def get_kelvin(self):
#         return KelModel.objects.all()
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
