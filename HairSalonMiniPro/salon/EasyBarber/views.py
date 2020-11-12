from django.shortcuts import render,get_object_or_404
from .models import *
from django.http import HttpResponse
# Create your views here.


def welcome(request):
    return render(request,'EasyBarber/welcome.html',{"news":'get flat 50% discount on your first booking'})

def user_reg(request):

    return render(request,'EasyBarber/user.html',{'users':Customer.objects.all()})











