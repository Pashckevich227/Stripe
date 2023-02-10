from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.http import HttpResponse
from .models import Item

import stripe
stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"


def create_checkout_session(request, pk):
    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': 'Telephone',
                },
                'unit_amount': Item.objects.get(pk=1),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://localhost:8000/item/1',
        cancel_url='http://localhost:8000/item/1',
    )
    return HttpResponse(session.id)


class Buy(DetailView):
    model = Item
    template_name = 'buy.html'
