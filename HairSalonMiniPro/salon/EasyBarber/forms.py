#This file is created to have a login/signup page for new customers

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import *



class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:

	    model = User
	    fields = ["username", "email", "password1", "password2","first_name","last_name"]



class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['app_no','shop_name','emp_name','rating','comment']



class PayNow(ModelForm):



    class Meta:
        model = Payment
        fields = ['pay_id','app_no','amt']





