from django.urls import path
from .views import Buy, create_checkout_session

urlpatterns = [
    path('item/<int:pk>', Buy.as_view()),
    path('buy/<int:pk>', create_checkout_session),
]
