import django_filters
from django_filters import DateFilter
from .models import *

class BookFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date", lookup_expr='gte')
    end_date = DateFilter(field_name="date", lookup_expr='lte')
    class Meta:
        model=Appointment
        fields=['cust_name','shop_name','emp_name','date','time','service_type','service_category']
        exclude=['date']

class RevFilter(django_filters.FilterSet):

    class Meta:
        model = Review
        fields = ['cust_name', 'shop_name', 'emp_name','rating']



