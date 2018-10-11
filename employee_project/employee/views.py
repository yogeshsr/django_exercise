
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Employee

def index(request):

    # return HttpResponse("Hello, world. You're at the employee index.")

    employees = Employee.objects.all()
    context = {
        'object_list': employees
    }

    template = loader.get_template('employee/employee_list.html')


    return HttpResponse(template.render(context, request))

    # shorcut
    # return render(request, 'employee/index.html', context)











