from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import FinancialStatementType, FinancialStatement, FinancialStatementLineSequence


class Financials(LoginRequiredMixin, ListView):
    context_object_name = 'financials'
    template_name = "financials/financial_statement.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'{self.financial_statement.pk}. {self.financial_statement.name}'
        context['id'] = self.financial_statement.pk
        return context
    
    def get_queryset(self):
        self.financial_statement = get_object_or_404(FinancialStatement, id=self.kwargs["financial_statement"])
        return FinancialStatementLineSequence.objects.filter(financial_statement=self.financial_statement)
    
