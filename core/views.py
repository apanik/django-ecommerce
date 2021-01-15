from django.shortcuts import render
from .models import Item, OrderItem, Order


def index(request):
    context = {
        'Items': Item.objects.all()
    }
    return render(request,template_name="home-page.html",context=context)
