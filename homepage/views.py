from django.shortcuts import render
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
    one_v_one_price = 1.2548
    four_producer_price = 4.2548
    eight_producer_price = 8.2548
    if request.method == 'POST':
        if 'one_vs_one' in request.POST:
            return render(request, 'buy-in.html', {'buy_in_type': '1 vs 1', 'buy_in_price': one_v_one_price})
        elif 'four_producer' in request.POST:
            return render(request, 'buy-in.html', {'buy_in_type': '4 Tour Producer', 'buy_in_price': four_producer_price})
        elif 'eight_producer' in request.POST:
            return render(request, 'buy-in.html', {'buy_in_type': '8 Tour Producer', 'buy_in_price': eight_producer_price})


def one_vs_one_buy_in(request):
    return render(request, '1_v_1_buy_in.html')


def submit_music(request):
    return render(request, 'submit_music.html')


def four_tour_producer_chart(request):
    return render(request, '4_tour_producer_chart.html')


def eight_tour_producer_chart(request):
    return render(request, '8_tour_producer_chart.html')
