from django.shortcuts import render

# Create your views here.


def homepage(request):
    return render(request, 'homepage.html')


def buy_in(request):
    return render(request, 'buy_in.html')


def one_vs_one_buy_in(request):
    return render(request, '1_v_1_buy_in.html')
