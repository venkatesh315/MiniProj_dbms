from django.urls import path
from . import views

urlpatterns=[
    path('customer',views.user_reg,name='customer'),

]
