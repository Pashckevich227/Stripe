from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Item

import stripe
stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"


def create_checkout_session(request):
    session = stripe.checkout.Session.create()
    return redirect(session.url, code=303)


class Buy(DetailView):
    model = Item
    template_name = 'buy.html'
