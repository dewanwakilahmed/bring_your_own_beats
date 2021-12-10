from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from login_register.views import login_register
from django.contrib import messages

# Create your views here.


def homepage(request):
    return render(request, 'homepage.html')


def logout(request):
    auth.logout(request)
    messages.info(request, 'Logged Out Successfully!')
    return login_register(request)


def buy_in(request):
    return render(request, 'buy_in.html')


def one_vs_one_buy_in(request):
    return render(request, '1_v_1_buy_in.html')


def submit_music(request):
    return render(request, 'submit_music.html')


def four_tour_producer_chart(request):
    return render(request, '4_tour_producer_chart.html')


def eight_tour_producer_chart(request):
    return render(request, '8_tour_producer_chart.html')
