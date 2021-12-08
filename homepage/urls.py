from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('buy-in/', views.buy_in, name='buy_in'),
]
