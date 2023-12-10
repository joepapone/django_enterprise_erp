from django.urls import path

from . import views

urlpatterns = [
    path('hr/department_list', views.deparment_list, name="department_list"),
    path('hr/department_add', views.department_add, name="department_add"),
    #path('hr/department_udepdate/<int:department_id>/', views.department_update, name="department_update"),
    path('hr/department_delete/<int:department_id>/', views.department_delete, name="department_delete"),
]
