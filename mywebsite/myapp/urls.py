from .views import Homepage
from django.urls import path

urlpatterns = [
    path('', Homepage),
]
