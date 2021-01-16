from django.urls import path
from .views import IndexListView, ItemDetailView, checkout, add_to_chart, remove_from_cart
urlpatterns = [
    path('', IndexListView.as_view(), name='indexView'),
    path('product/<slug:slug>', ItemDetailView.as_view(), name='ItemDetailView'),
    path('checkout', checkout, name='Checkout'),
    path('add_to_chart/<slug:slug>', add_to_chart, name='add_to_chart'),
    path('remove_to_chart/<slug:slug>', remove_from_cart, name='remove_to_chart'),

]
