from datetime import date

from django.forms import ModelForm, DateInput, TimeInput,TextInput,IntegerField
from django.core.exceptions import ValidationError

from .models import *


class ScheduleForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ['app_no','shop_name','emp_name','date','time','service_type','service_category']

        widgets = {

            'date':DateInput(attrs={"type":"date"}),
            'time':TimeInput(attrs={"type":"time"}),

        }


    def clean_date(self):
        d=self.cleaned_data.get("date")
        if d < date.today():
            raise ValidationError("Appointments cannot be booked for the past date")
        return d


