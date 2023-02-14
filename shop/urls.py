from django.urls import path
from .views import (Buy,
                    create_checkout_session,
                    ShopListView,
                    OrderCreateView,
                    create_basket)

urlpatterns = [
    path('', ShopListView.as_view()),
    path('item/<int:pk>', Buy.as_view(), name='item'),
    path('buy/<int:pk>', create_checkout_session),
    path('order/', OrderCreateView.as_view()),
    path('order/checkout', create_basket)
]
