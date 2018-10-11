from django.urls import path
from django.conf.urls import url

from . import views, forms_view
from .views_class import EmployeeList, EmployeeListGeneric

urlpatterns = [

    path('', views.index, name='index'),
    
    path('views_class/', EmployeeList.as_view()),
    path('views_class_generic/', EmployeeListGeneric.as_view()),

	path('<int:pk>/', forms_view.EmployeeDetailView.as_view(), name='employee_details'),

    path('new/', forms_view.get_employee, name="new_employee"),
]