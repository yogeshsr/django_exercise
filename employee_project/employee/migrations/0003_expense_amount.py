# Generated by Django 2.1.1 on 2018-10-07 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20181007_0549'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]