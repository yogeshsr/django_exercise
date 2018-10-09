from django.db import models

from employee.models import Employee

class Project(models.Model):
    project_name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, null=True)
    employees = models.ManyToManyField(Employee)
    # TODO how to find which project and emp belongs to

    def __str__(self):
        return self.project_name
