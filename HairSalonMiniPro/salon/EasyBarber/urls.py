from django.urls import path
from . import views

urlpatterns=[
    path('owner_signup',views.owner_signup,name='fos'),
    path('cust_signup',views.cust_signup,name='fcs'),
    path('about_us',views.about_us,name='about')
]
