from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('catalog', views.catalog, name='catalog'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('calc', views.calc, name='calc'),
]
