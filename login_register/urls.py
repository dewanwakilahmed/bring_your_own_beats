from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_register, name='login_register')
]
