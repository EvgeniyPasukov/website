from django.urls import path
from . import views

urlpatterns = [
    path('', views.CatalogView.as_view(), name='catalog'),
    path('filter/', views.Filters.as_view(), name='filter'),
    path('<slug:slug>/', views.CatalogDetailView.as_view(), name='details'),
]
