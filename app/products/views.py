from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Product


# --- Products --- #
class ProductList(LoginRequiredMixin, ListView):
    model = Product
    context_object_name = 'products'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = context['products']
        return context
    
class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    context_object_name = 'product'
    
    '''
    def get_queryset(self):
        base_qs = super(ProductDetail, self).get_queryset()
        return base_qs.filter(user=self.request.user)
    '''

class ProductCreate(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['name','description']
    success_url = reverse_lazy('products')
    

    def form_valid(self, form):
        messages.success(self.request, "The product was created successfully.")
        return super(ProductCreate,self).form_valid(form)
           
class ProductUpdate(LoginRequiredMixin, UpdateView):
    model = Product
    fields = ['name','description']
    success_url = reverse_lazy('products')
    
    def form_valid(self, form):
        messages.success(self.request, "The product was updated successfully.")
        return super(ProductUpdate,self).form_valid(form)
    
class ProductDelete(LoginRequiredMixin, DeleteView):
    model = Product
    context_object_name = 'product'
    success_url = reverse_lazy('products')
    
    def form_valid(self, form):
        messages.success(self.request, "The product was deleted successfully.")
        return super(ProductDelete,self).form_valid(form)

