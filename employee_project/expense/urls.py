from django.urls import path
from django.conf.urls import url

from . import views, views_class

urlpatterns = [
    url(r'^api/expense/$', views.expense),
    url(r'^api/expense/view_class/$', views_class.ExpenseListClassView.as_view()),
    url(r'^api/expense/view_mixin_class/$', views_class.ExpenseList.as_view()),
    url(r'^api/expense/view_generic_class/$', views_class.ExpenseListGeneric.as_view()),

]