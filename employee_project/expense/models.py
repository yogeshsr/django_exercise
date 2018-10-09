from django.db import models

from employee.models import Employee

class Expense(models.Model):
    # implicit PK
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    expense_name = models.CharField(max_length=200)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return self.expense_name
