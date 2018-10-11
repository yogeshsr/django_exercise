from django import forms

class EmployeeForm(forms.Form):
    name = forms.CharField(label='Employee name', max_length=100)