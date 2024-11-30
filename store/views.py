from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to the Store!</h1>")

def customer_list(request):
    # Example logic for customer_list view
    return HttpResponse("<h2>Customer List</h2>")

def order_list(request):
    # Example logic for order_list view
    return HttpResponse("<h2>Order List</h2>")
