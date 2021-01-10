from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class Shop_Owner(models.Model):
    own_id = models.IntegerField(primary_key=True)
    own_name=models.CharField(max_length=50)
    own_email = models.EmailField(max_length=50)
    own_phone=models.IntegerField()
    shop_name = models.CharField(max_length=50,unique=True)
    shop_address= models.TextField(max_length=100,unique=True)
    own_gender=models.CharField(max_length=6,choices=(('Male','male'),('Female','female')))

    def __str__(self):
        return f'{self.shop_name}'

class Shop_Barber(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    emp_name=models.CharField(max_length=50,unique=True)
    emp_email = models.EmailField(max_length=50)
    emp_phone=models.IntegerField()
    shop_name = models.ForeignKey(Shop_Owner,on_delete=models.CASCADE,to_field='shop_name',related_name="sb_shop")
    shop_address= models.ForeignKey(Shop_Owner,on_delete=models.CASCADE,to_field='shop_address',related_name="sb_address")
    emp_gender=models.CharField(max_length=6,choices=(('Male','male'),('Female','female')))

    def __str__(self):
        return f'{self.emp_name}({self.shop_name})'

class Customer(models.Model):
    cust_id=models.IntegerField(primary_key=True)
    cust_name=models.CharField(max_length=50,unique=True)
    cust_email=models.EmailField(max_length=50,unique=True)
    cust_phone=models.IntegerField()
    cust_address=models.TextField(max_length=100)
    cust_gender=models.CharField(max_length=6,choices=(('Male','male'),('Female','female')))

    def __str__(self):
        return f'{self.cust_name}'




class Appointment(models.Model):
    app_no=models.CharField(primary_key=True,max_length=100,blank=True, unique=True, default=uuid.uuid4)
    cust_name=models.CharField(max_length=50)
    cust_email=models.EmailField(max_length=50)
    shop_name=models.ForeignKey(Shop_Owner,on_delete=models.SET_NULL,null=True,to_field='shop_name',related_name='app_shop',)
    emp_name=models.ForeignKey(Shop_Barber,on_delete=models.SET_NULL,null=True,to_field='emp_name',related_name='app_emp')
    date=models.DateField()
    time=models.TimeField()
    service_type=models.CharField(max_length=4,choices=(('Shop','shop'),('Home','home')))
    service_category=models.CharField(max_length=50,choices=(('Haircut','haircut'),('Massage','massage'),
                                                             ('Hair Colour','hair colour'),('Shave','shave'),
                                                             ('Facial','facial')))

    def __str__(self):
        return f'{self.cust_name} on {self.date} at {self.time}'



class Payment(models.Model):
    pay_id = models.CharField(primary_key=True,max_length=100, blank=True, unique=True, default=uuid.uuid4)
    cust_name = models.CharField(max_length=50)
    app_no = models.ForeignKey(Appointment, to_field='app_no', on_delete=models.SET_NULL, null=True)
    amt=models.IntegerField()

    def __str__(self):
        return f'Payment id:{self.pay_id} for appointment:{self.app_no}'

class Review(models.Model):
    review_id=models.CharField(primary_key=True,max_length=100,blank=True, unique=True, default=uuid.uuid4)
    app_no=models.ForeignKey(Appointment,on_delete=models.SET_NULL,null=True,to_field='app_no',related_name='rev_no')
    cust_name=models.CharField(max_length=50)
    shop_name = models.ForeignKey(Shop_Owner, on_delete=models.SET_NULL, null=True, to_field='shop_name',related_name='rev_shop')
    emp_name = models.ForeignKey(Shop_Barber, on_delete=models.SET_NULL, null=True, to_field='emp_name', related_name='rev_emp')
    rating=models.IntegerField(choices=((1,1),(2,2),(3,3),(4,4),(5,5)))
    comment=models.TextField(max_length=300)

    def __str__(self):
        return f'rating:{self.rating} given for appointment {self.app_no}'
