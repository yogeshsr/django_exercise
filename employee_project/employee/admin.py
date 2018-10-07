from django.contrib import admin

from .models import Employee, Expense, Project

admin.site.register(Employee)
admin.site.register(Expense)
admin.site.register(Project)