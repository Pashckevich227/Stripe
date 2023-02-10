from django.urls import path
from .views import Buy

urlpatterns = [
    path('buy/', Buy.as_view(), name='buy'),
]