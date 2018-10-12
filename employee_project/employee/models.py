from django.db import models


class Employee(models.Model):

    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=200, unique=True, null=False)
    city = models.CharField(max_length=200, null=True)


    def __str__(self):
        return self.name


