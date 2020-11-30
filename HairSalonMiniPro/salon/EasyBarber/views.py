from django.shortcuts import render,get_object_or_404,redirect
from django.forms import modelform_factory
from .models import *
from EasyBarber.forms import RegisterForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from EasyBarber.forms_book import ScheduleForm
from django.core.mail import send_mail
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

        if request.method == 'POST':

            form_app = ScheduleForm(request.POST)
            if form_app.is_valid():
                email_id = request.POST.get('cust_email', False)
                time_msg=request.POST.get('time',False)
                date_msg=request.POST.get('date',False)
                inst=form_app.save(commit=False)
                name=request.user.get_full_name()
                inst.cust_name=name
                inst.save()
                send_mail(
                'EasyBarber Appointment Confirmation',  #Subject
                'Hello '+ name + ' Your appointment on ' + date_msg + 'at '+ time_msg + ' has been confirmed',#message
                'EasyBarber@gmail.com', #from
                [email_id],#to_email
                )
                return render(request, 'EasyBarber/schedule.html',{"form": form_app, "confirm": name})

        else:
            form_app = ScheduleForm()
        return render(request,'EasyBarber/schedule.html',{"form": form_app})


 #  if request.method == "POST":
   #     form_app = ScheduleForm(request.POST)
    #    if form_app.is_valid():
     #       temp=form_app.save(commit=False)
      #      get_uname = request.user.username
       #     temp.cust_name = get_uname
        #    temp=form_app.save()
         #   return redirect(welcome)






#candidate.user = UserProfile.objects.get(user=self.request.user)












