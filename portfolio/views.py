from django.views.generic import ListView, DetailView
from .models import Portfolio


class PortfolioView(ListView):
    model = Portfolio
    queryset = Portfolio.objects.all()
    template_name = 'portfolio/portfolio.html'
    context_object_name = 'item_list'


class PortfolioDetailView(DetailView):
    model = Portfolio
    slug_field = 'url'
    context_object_name = 'detail'
