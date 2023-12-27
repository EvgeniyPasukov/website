from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Catalog


class TaskList(ListView):
    model = Catalog
    context_object_name = 'tasks'