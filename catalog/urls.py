from django.urls import path
from . import views
from .views import CategoryListView, SubCategoryListView, ProductListView, ProductDetailView

urlpatterns = [
    path('', CategoryListView.as_view(), name='category_list'),
    path('<slug:category_slug>/subcategories/', SubCategoryListView.as_view(), name='subcategory_list'),
    path('subcategories/<int:subcategory_id>/products/', ProductListView.as_view(), name='product_list'),
    path('products/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),  # Изменили на slug

    # path('', CategoryListView.as_view(), name='category_list'),
    # path('<slug:slug>/', SubCategoryListView.as_view(), name='subcategory_list'),
    # path('<slug:category_slug>/<slug:slug>/', ProductListView.as_view(), name='product_list'),
    # path('<slug:category_slug>/<slug:subcategory_slug>/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),  # Изменили на slug




    # path('', views.CatalogView.as_view(), name='catalog'),
    # path('filter/', views.Filters.as_view(), name='filter'),
    # path('<slug:slug>/', views.CatalogDetailView.as_view(), name='details'),
]


