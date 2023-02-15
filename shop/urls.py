from django.urls import path
from .views import (Buy,
                    create_checkout_session,
                    ShopListView,
                    OrderView,
                    create_basket,
                    OrderCreateView,
                    OrderDeleteView)

urlpatterns = [
    path('', ShopListView.as_view()),
    path('item/<int:pk>', Buy.as_view(), name='item'),
    path('buy/<int:pk>', create_checkout_session),
    path('order/', OrderView.as_view(), name='order'),
    path('order/checkout', create_basket),
    path('create/<int:pk>/order', OrderCreateView.as_view(), name='order_new'),
    path('order/<int:pk>/delete/', OrderDeleteView.as_view(), name='order_delete'),
]
