from django.urls import path
from .views import Buy, create_checkout_session, ShopListView

urlpatterns = [
    path('', ShopListView.as_view()),
    path('item/<int:pk>', Buy.as_view(), name='item'),
    path('buy/<int:pk>', create_checkout_session),
]
