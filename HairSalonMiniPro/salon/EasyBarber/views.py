from django.shortcuts import render,get_object_or_404,redirect , HttpResponseRedirect , reverse
from django.forms import modelform_factory
from .models import *
from EasyBarber.forms import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from EasyBarber.forms_book import ScheduleForm
from django.core.mail import send_mail
from django.contrib.auth.models import User


from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import ListView



from django.views.generic import View
from django.contrib import messages

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




@login_required(login_url='/login')
def my_appointments(request):

        if request.method == 'POST':

            form_app = ScheduleForm(request.POST)
            if form_app.is_valid():

                time_msg=request.POST.get('time',False)
                date_msg=request.POST.get('date',False)
                current_user=request.user
                user = User.objects.get(id=current_user.id)
                user_email = user.email
                inst=form_app.save(commit=False)
                name=request.user.get_full_name()

                inst.cust_name=name
                inst.cust_email=user_email
                inst.save()
                request.session["schedule_form"] = request.POST.dict()  # save the form as a dict in request.sessions

                send_mail(
                'EasyBarber Appointment Confirmation',  #Subject
                'Hello '+ name + ' Your appointment on ' + date_msg + ' at '+ time_msg + ' has been confirmed',#message
                'EasyBarber@gmail.com', #from
                [user_email],#to_email
                )

                return redirect(pay_now)

        else:
            form_app = ScheduleForm()
        return render(request,'EasyBarber/schedule.html',{"form": form_app})


def display_booked(request):
    return render(request, 'EasyBarber/list_booked.html', {'booked': Appointment.objects.all()})






@login_required(login_url='/login')
def my_reviews(request):

        if request.method == 'POST':

            form_rev = ReviewForm(request.POST)
            if form_rev.is_valid():

                inst=form_rev.save(commit=False)
                name=request.user.get_full_name()

                inst.cust_name=name
                inst.save()

                return render(request, 'EasyBarber/reviews.html', {"form": form_rev, "rev_name": name})

        else:
            form_rev = ReviewForm()
        return render(request,'EasyBarber/reviews.html',{"form": form_rev})




def display_feedbacks(request):
    return render(request, 'EasyBarber/list_feedbacks.html', {'feedbacks': Review.objects.all()})




def pay_now(request):

    if request.method == "POST":

        form_pay = PayNow(request.POST)
        if form_pay.is_valid():
            fp=form_pay.save(commit=False)
            name = request.user.get_full_name()
            fp.cust_name = name


            fp.save()
            request.session["payment_form"] = request.POST.dict()



            return render(request, 'EasyBarber/paid.html', {'confirm': name})

    else:
        form_data = request.session.pop('schedule_form', {})

        pay_appno = form_data.get("app_no")
        pay_service = form_data.get("service_category")
        if pay_service == 'Haircut':
            pay_amt=250
        elif pay_service == 'Massage':
            pay_amt=200
        elif pay_service == 'Hair Colour':
            pay_amt=300
        elif pay_service == 'Shave':
            pay_amt=150
        else:
            pay_amt=400
        form_pay = PayNow(
            initial={"app_no": pay_appno, "amt":pay_amt})  # initialize the form with the data

    return render(request, 'EasyBarber/paid.html', {'form': form_pay})




def render_pdf_view(request):
    paid_data = request.session.pop('payment_form', {})
    pay_appno = paid_data.get("app_no")
    pay_no = paid_data.get("pay_id")
    pay_amt=paid_data.get("amt")
    name=request.user.get_full_name()
    template_path = 'EasyBarber/pdf1.html'
    context = {'customer': name ,'application': pay_appno ,'payment':pay_no, 'money': pay_amt}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Invoice.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
     html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response






