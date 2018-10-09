
from django.http import HttpResponse
from django.template import loader

from .models import Employee

def index(request):
    # return HttpResponse("Hello, world. You're at the employee index.")

    employees = Employee.objects.all()
    context = {
        'employees': employees
    }

    template = loader.get_template('employee/index.html')


    return HttpResponse(template.render(context, request))








