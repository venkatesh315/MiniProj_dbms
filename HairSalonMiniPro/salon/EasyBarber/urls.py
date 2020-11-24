from django.urls import path
from . import views

urlpatterns=[
    path('home',views.welcome,name='home'),
    path('owner_signup',views.owner_signup,name='fos'),
    path('cust_signup',views.cust_signup,name='fcs'),
    path('about_us',views.about_us,name='about'),
    path('cust_pass',views.register_cust,name='cust_pass'),
    path('own_pass',views.register_owner,name='own_pass'),
    path('shop_names',views.list_of_shops,name='store'),
]
