from django.shortcuts import render
from .models import Item, OrderItem, Order
from django.views.generic import ListView, DetailView


class IndexListView(ListView):
    model = Item
    template_name = "home-page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ItemDetailView(DetailView):
    model = Item
    template_name = "product-page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def checkout(request):
    return render(request, 'checkout-page.html')
