from django import forms
from .models import *


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'email', 'mobileno', 'password', 'city', 'profile_image', 'gender']


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['appointment_id', 'reason', 'date', 'time']


class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = ['work', 'work_type', 'work_price']


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['name', 'price', 'description', 'img', 'quantity']
