from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Shop_Owner)
admin.site.register(Shop_Barber)
admin.site.register(Customer)
admin.site.register(Appointment)
admin.site.register(Payment)
admin.site.register(Reviews)
