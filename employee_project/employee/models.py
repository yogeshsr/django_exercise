from django.db import models
from django.utils import timezone
import datetime


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Expense(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    expense_name = models.CharField(max_length=200)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return self.expense_name


class Project(models.Model):
    project_name = models.CharField(max_length=200)
    employees = models.ManyToManyField(Employee)
    # TODO how to find which project and emp belongs to

    def __str__(self):
        return self.project_name

# Create an Django project for Employee, Project and Expense report
# Emp -> Prj (m to m) | full/part time
# Emp -> expense_report (one to one)
# expense_report -> expense_item (one to many)
