from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalog_list, name='catalog_list'),
    path('details/', views.details, name='details')
]
