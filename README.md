# Django hands on
```
# Ensure you have Python 3.6.5
python --version

clone this repo

cd django-exercise
virtualenv -p python3 virt_env3

source virt_env3/bin/activate
pip install -r requirnments.txt

cd employee_project/

python manage.py migrate

# Create admin user and password
python manage.py createsuperuser

python manage.py runserver

# Create new Employee, Project and Expense using admin console
http://127.0.0.1:8000/admin/

# Browse the app and api
http://127.0.0.1:8000/employee/
http://127.0.0.1:8000/employee/new/
http://127.0.0.1:8000/employee/1/

http://127.0.0.1:8000/expense/api/expense/


```