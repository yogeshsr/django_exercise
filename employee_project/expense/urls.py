from django.urls import path
from django.conf.urls import re_path

from . import views, views_class

urlpatterns = [
	# url is alias and likely to be depricated
    re_path(r'^api/expense/$', views.expense),
    re_path(r'^api/expense/view_class/$', views_class.ExpenseListClassView.as_view()),
    re_path(r'^api/expense/view_mixin_class/$', views_class.ExpenseList.as_view()),
    re_path(r'^api/expense/view_generic_class/$', views_class.ExpenseListGeneric.as_view()),

]