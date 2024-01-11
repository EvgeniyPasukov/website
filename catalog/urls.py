from django.urls import path
from . import views

urlpatterns = [
    path('', views.CatalogView.as_view(), name='catalog'),
    path('<slug:slug>/', views.CatalogDetailView.as_view(), name='details'),
]
