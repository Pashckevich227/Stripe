from django.shortcuts import render
import stripe
from django.views.generic import ListView

from .models import Item

stripe.api_key = 'sk_test_4eC39HqLyjWDarjtT1zdp7dc'


class Buy(ListView):
    model = Item
    template_name = 'buy.html'

