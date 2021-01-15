from django.urls import path
from .views import IndexListView, ItemDetailView ,checkout
urlpatterns = [
    path('', IndexListView.as_view(), name='indexView'),
    path('product/<slug:slug>', ItemDetailView.as_view(), name='ItemDetailView'),
    path('checkout', checkout, name='Checkout'),

]
