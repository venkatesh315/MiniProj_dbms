from datetime import date

from django.forms import ModelForm, DateInput, TimeInput,TextInput,IntegerField
from django.core.exceptions import ValidationError

from .models import *


class ScheduleForm(ModelForm):
    class Meta:
        model = Appointment
        #fields = ['cust_name','cust_email','shop_name','emp_name','date','time','service_type','service_category']
        fields='__all__'
        widgets = {

            'date':DateInput(attrs={"type":"date"}),
            'time':TimeInput(attrs={"type":"time"})
        }



    def clean_date(self):
        d=self.cleaned_data.get("date")
        if d < date.today():
            raise ValidationError("Appointments cannot be booked for the past date")
        return d

    #  def __init__(self, *args, **kwargs):
    #         self._user = kwargs.pop('user')
    #        super(ScheduleForm, self).__init__(*args, **kwargs)

    # def save(self, commit=True):
    #        inst = super(ScheduleForm, self).save(commit=False)
    #       obj=Appointment
    #      obj.name_user = self._user
    #     #obj.cust_name=self._user
    #    if commit:
    #       inst.save()
    #      self.save_m2m()
    # return inst


