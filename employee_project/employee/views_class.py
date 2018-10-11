
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from django.views.generic import ListView

from .models import Employee


class EmployeeList(ListView):

    def get(self, request, *args, **kwargs):
        employees = Employee.objects.all()
        context = {
            'object_list': employees
        }

        return render(request, 'employee/employee_list.html', context)


class EmployeeListGeneric(ListView):
    model = Employee
    # the below is implicit
    template_name = 'employee/employee_list.html'

    # adding extra context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employee_list'] = Employee.objects.all()
        return context









