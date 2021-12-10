from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('homepage/logout/', views.logout,
         name='logout'),
    path('homepage/buy-in', views.buy_in, name='buy_in'),
    path('homepage/1-v-1-buy-in',
         views.one_vs_one_buy_in, name='one_vs_one_buy_in'),
    path('submit-music/', views.submit_music, name='submit_music'),
    path('homepage/purchase-ticket', views.four_tour_producer_chart,
         name='four_tour_producer_chart'),
    path('8-tour-producer-chart/', views.eight_tour_producer_chart,
         name='eight_tour_producer_chart'),
]
