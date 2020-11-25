from django.shortcuts import render,get_object_or_404,redirect
from django.forms import modelform_factory
from .models import *
from EasyBarber.forms import RegisterForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from EasyBarber.forms_book import ScheduleForm

# Create your views here.


def welcome(request):
    return render(request,'EasyBarber/welcome.html')

def about_us(request):
    return render(request,'EasyBarber/about.html')


Owner_Signup=modelform_factory(Shop_Owner,exclude=['own_id'])

def owner_signup(request):
    if request.method == "POST":
        form_os = Owner_Signup(request.POST)
        if form_os.is_valid():
            form_os.save()
            return redirect(register_owner)

    else:
        form_os = Owner_Signup()
    return render(request,'EasyBarber/owner_new.html', {"form": form_os})


CustSignUp=modelform_factory(Customer,exclude=['cust_id'])

def cust_signup(request):
    if request.method == "POST":
        form_cs=CustSignUp(request.POST)
        if form_cs.is_valid():
            form_cs.save()
            return redirect(register_cust)

    else:
        form_cs=CustSignUp()
    return render(request,'EasyBarber/cust_new.html',{"form":form_cs})



def register_cust(request):
        if request.method == "POST":
            form_c = RegisterForm(request.POST)
            if form_c.is_valid():
                form_c.save()
                return redirect(welcome)

        else:
            form_c = RegisterForm()
        return render(request,"EasyBarber/cust_password.html",{"form":form_c})


def list_of_shops(request):
    return render(request,"EasyBarber/shop_list.html")


def register_owner(request):
        if request.method == "POST":
            form_ow = RegisterForm(request.POST)
            if form_ow.is_valid():
                form_ow.save()
                return redirect(welcome)

        else:
            form_ow = RegisterForm()
        return render(request, "EasyBarber/own_password.html", {"form": form_ow})




@login_required
def my_appointments(request):
    if request.method == "POST":
        form_app =ScheduleForm(request.POST)
        if form_app.is_valid():
            form_app.save()
            return redirect(welcome)

    else:
        form_app = ScheduleForm()
    return render(request,'EasyBarber/schedule.html', {"form":form_app})















