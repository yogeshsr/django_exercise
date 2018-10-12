from django import forms

from django.forms import ModelForm

from .models import Employee

# class EmployeeForm(forms.Form):
#     name = forms.CharField(label='Employee name', max_length=100)

class EmployeeForm(ModelForm):
    class Meta:
    	model = Employee
    	fields = ['id','name', 'city']