from django.urls import path
from . import views
from .views import CategoryListView, SubCategoryListView, ProductListView, ProductDetailView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:category_id>/subcategories/', SubCategoryListView.as_view(), name='subcategory_list'),
    path('subcategories/<int:subcategory_id>/products/', ProductListView.as_view(), name='product_list'),
    path('products/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),  # Изменили на slug

    # rabochij variant
    # path('', views.CategoryListView.as_view(), name='category_list'),
    # path('<str:category>/', views.SubCategoryListView.as_view(), name='subcategory_list'),
    # path('<str:category>/<str:subcategory>/', views.CatalogBySubCategories.as_view(), name='product_list'),
    # end


    # path('', views.CatalogView.as_view(), name='catalog'),
    # path('filter/', views.Filters.as_view(), name='filter'),
    # path('<slug:slug>/', views.CatalogDetailView.as_view(), name='details'),
]


