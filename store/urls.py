from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # Default route for the store root
    path("customers/", views.customer_list, name="customer_list"),
    path("orders/", views.order_list, name="order_list"),
]



