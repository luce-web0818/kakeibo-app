from django.urls import path
from . import views

urlpatterns=[
    path('',views.home, name='home'),
    path('expenses/',views.expense_list, name='expense_list'),
    path('expenses/add/',views.expense_create, name='expense_create'),
    path('expenses/delete/<int:expense_id>/', views.expense_delete, name='expense_delete'),
    path('expenses/edit/<int:expense_id>/', views.expense_edit, name='expense_edit'),
]