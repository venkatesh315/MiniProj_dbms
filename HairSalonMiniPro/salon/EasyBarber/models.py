from django.db import models

# Create your models here.

class Shop_Owner(models.Model):
    own_id = models.IntegerField(primary_key=True)
    own_name=models.CharField(max_length=50)
    own_email = models.EmailField(max_length=50)
    own_phone=models.IntegerField()
    shop_name = models.CharField(max_length=50,unique=True)
    shop_address= models.TextField(max_length=100,unique=True)
    own_gender=models.CharField(max_length=6)

    def __str__(self):
        return f'Owner: {self.own_id}'
class Shop_Barber(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    emp_name=models.CharField(max_length=50,unique=True)
    emp_email = models.EmailField(max_length=50)
    emp_phone=models.IntegerField()
    shop_name = models.ForeignKey(Shop_Owner,on_delete=models.CASCADE,to_field='shop_name',related_name="+")
    shop_address= models.ForeignKey(Shop_Owner,on_delete=models.CASCADE,to_field='shop_address',related_name="+")
    emp_gender=models.CharField(max_length=6)

    def __str__(self):
        return f'Barber: {self.emp_id}'



class Customer(models.Model):
    cust_id=models.IntegerField(primary_key=True)
    cust_name=models.CharField(max_length=50,unique=True)
    cust_email=models.EmailField(max_length=50)
    cust_phone=models.IntegerField()
    cust_address=models.TextField(max_length=100)
    cust_gender=models.CharField(max_length=6)

    def __str__(self):
        return f'Customer: {self.cust_id}'


class Appointment(models.Model):
    app_no=models.IntegerField()
    cust_name=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,to_field='cust_name',related_name='+')
    shop_name=models.ForeignKey(Shop_Owner,on_delete=models.SET_NULL,null=True,to_field='shop_name',related_name='+',)
    emp_name=models.ForeignKey(Shop_Barber,on_delete=models.SET_NULL,null=True,to_field='emp_name',related_name='+')
    app_date=models.DateField()
    app_time=models.TimeField()
    service_type=models.CharField(max_length=4,choices=(('Shop','shop'),('Home','home')))
    service_category=models.CharField(max_length=50,choices=(('Haircut','haircut'),('Massage','massage'),
                                                             ('Hair Colour','hair colour'),('Shave','shave'),
                                                             ('Facial','facial')))

    def __str__(self):
        return f'AppNum:{self.app_no},Customer:{self.cust_name} on {self.app_time}'

class Payment(models.Model):
    pay_id=models.IntegerField()
    app_no=models.ForeignKey(Appointment,on_delete=models.SET_NULL,null=True)
    amt=models.IntegerField()

    def __str__(self):
        return f'Payment id:{self.pay_id} for appointment:{self.app_no}'

class Reviews(models.Model):
    app_no=models.ForeignKey(Appointment,on_delete=models.SET_NULL,null=True)
    rating=models.IntegerField(choices=((1,'one'),(2,'two'),(3,'three'),(4,'four'),(5,'five')))
    comment=models.TextField(max_length=300)

    def __str__(self):
        return f'rating:{self.rating} given for appointment {self.app_no}'
