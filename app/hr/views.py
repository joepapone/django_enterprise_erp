from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Department, Employee


# --- Departments --- #
class DepartmentList(LoginRequiredMixin, ListView):
    model = Department
    context_object_name = 'departments'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['departments'] = context['departments']
        return context
    
class DepartmentDetail(LoginRequiredMixin, DetailView):
    model = Department
    context_object_name = 'department'
    
    '''
    def get_queryset(self):
        base_qs = super(DepartmentDetail, self).get_queryset()
        return base_qs.filter(user=self.request.user)
    '''

class DepartmentCreate(LoginRequiredMixin, CreateView):
    model = Department
    fields = ['name','description']
    success_url = reverse_lazy('departments')
    

    def form_valid(self, form):
        messages.success(self.request, "The department was created successfully.")
        return super(DepartmentCreate,self).form_valid(form)
           
class DepartmentUpdate(LoginRequiredMixin, UpdateView):
    model = Department
    fields = ['name','description']
    success_url = reverse_lazy('departments')
    
    def form_valid(self, form):
        messages.success(self.request, "The department was updated successfully.")
        return super(DepartmentUpdate,self).form_valid(form)
    
class DepartmentDelete(LoginRequiredMixin, DeleteView):
    model = Department
    context_object_name = 'department'
    success_url = reverse_lazy('departments')
    
    def form_valid(self, form):
        messages.success(self.request, "The department was deleted successfully.")
        return super(DepartmentDelete,self).form_valid(form)


# --- Employees --- #
class EmployeeList(LoginRequiredMixin, ListView):
    model = Employee
    context_object_name = 'employees'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employees'] = context['employees']
        return context
    
class EmployeeDetail(LoginRequiredMixin, DetailView):
    model = Employee
    context_object_name = 'employee'
    
    '''
    def get_queryset(self):
        base_qs = super(EmployeeDetail, self).get_queryset()
        return base_qs.filter(user=self.request.user)
    '''

class EmployeeCreate(LoginRequiredMixin, CreateView):
    model = Employee
    fields = ['name','surname']
    success_url = reverse_lazy('employees')
    

    def form_valid(self, form):
        messages.success(self.request, "The employee was created successfully.")
        return super(EmployeeCreate,self).form_valid(form)
           
class EmployeeUpdate(LoginRequiredMixin, UpdateView):
    model = Employee
    fields = ['name','surname']
    success_url = reverse_lazy('employees')
    
    def form_valid(self, form):
        messages.success(self.request, "The employee was updated successfully.")
        return super(EmployeeUpdate,self).form_valid(form)
    
class EmployeeDelete(LoginRequiredMixin, DeleteView):
    model = Employee
    context_object_name = 'employee'
    success_url = reverse_lazy('employees')
    
    def form_valid(self, form):
        messages.success(self.request, "The employee was deleted successfully.")
        return super(EmployeeDelete,self).form_valid(form)


        