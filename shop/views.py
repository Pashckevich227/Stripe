from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView, CreateView
from django.http import HttpResponse
from .models import Item, Order
import stripe
import environ
import os
from django.core import serializers
env = environ.Env()
environ.Env.read_env(os.path.join("/venv/Stripe/", '.env'))
stripe.api_key = env("STRIPE_API_KEY")


def create_checkout_session(request, pk):
    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'USD',
                'product_data': {
                    'name': 'Telephone',
                },
                'unit_amount': Item.objects.get(pk=pk),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://localhost:8000/item/1',
        cancel_url='http://localhost:8000/item/1',
    )
    return HttpResponse(session.id)

def create_basket(request):
    object_list = serializers.serialize("python", Order.objects.all())
    line_items = []

    for object in object_list:
        item_data = {
                'price_data': {
                    'currency': 'USD',
                    'product_data': {
                        'name': 'Telephone',
                    },
                    'unit_amount': Item.objects.get(pk=object['fields']['pk_item']),
                },
                'quantity': object['fields']['quantity'],
            }
        line_items.append(item_data)

    session = stripe.checkout.Session.create(
        line_items = line_items,
        mode='payment',
        success_url='http://localhost:8000/',
        cancel_url='http://localhost:8000/',
    )
    return HttpResponse(session.id)


class Buy(DetailView):
    model = Item
    template_name = 'buy.html'

class ShopListView(ListView):
    model = Item
    template_name = 'base.html'

class OrderCreateView(ListView):
    model = Order
    template_name = 'order.html'
