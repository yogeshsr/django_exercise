# Generated by Django 2.1.1 on 2018-10-07 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_project'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='project_employee',
            new_name='employees',
        ),
    ]
