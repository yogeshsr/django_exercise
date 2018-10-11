from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.views.generic import DetailView

from .forms import EmployeeForm
from .models import Employee

def get_employee(request):

    if request.method == 'POST':

        form = EmployeeForm(request.POST)
        if form.is_valid():
            
            # to debug
            # import pdb; pdb.set_trace()

            form.save()

            return HttpResponseRedirect('/employee')

    else:
        form = EmployeeForm()

    return render(request, 'employee/employee_form.html', {'form': form})

def get_employee_by_id(request, id):

    form = EmployeeForm(instance=Employee.objects.get(pk=id))
    return render(request, 'employee/employee_form.html', {'form': form})


class EmployeeDetailView(DetailView):

    queryset = Employee.objects.all()

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['employee'] = Employee.objects.get(pk=self.kwargs['pk'])
    #     return context

    # def get_object(self, **kwargs):
    #     obj = super().get_object()
        
    #     return obj


