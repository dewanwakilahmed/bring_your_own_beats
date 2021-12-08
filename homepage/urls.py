from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('buy-in/', views.buy_in, name='buy_in'),
    path('1-v-1-buy-in/', views.one_vs_one_buy_in, name='one_vs_one_buy_in'),
]
