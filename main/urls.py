from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowMainView.as_view(), name='home'),
    path('about', views.about, name='about'),
    path('catalog/', views.catalog, name='catalog'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('calc', views.calc, name='calc'),
    path('contacts', views.contacts, name='contacts'),
]
