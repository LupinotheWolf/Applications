from django import forms
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from .forms import *

#Homepage/Index View
def index(request):
    if not request.user.is_authenticated:
        return render(request, "budgets/login.html",)
    else:
        return render(request, "budgets/index.html", {
            'budgets': Transaction.objects.all(),
            'templates': Template.objects.all(),
        })

#Budget Overview Page
@login_required
def overview(request):
    templates = Template.objects.filter(account=request.user)
    budgets = Budget.objects.filter(account=request.user)
    return render(request, "budgets/overview.html", {
        'templates': templates,
        'budgets': budgets,
    })

#Class-Based Views
class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    def get_queryset(self):
        return Transaction.objects.filter(account=self.request.user)
class Transaction_Create(LoginRequiredMixin, CreateView):
    model = Transaction
    fields = ['name', 'amount', 'date', 'category', 'notes']
    def form_valid(self, form):
        form.instance.account = self.request.user
        return super().form_valid(form)
class TransactionDetailView(LoginRequiredMixin, DetailView):
    model = Transaction
    fields = ['name', 'amount', 'date', 'category', 'notes']
class Transaction_Update(LoginRequiredMixin, UpdateView):
    model = Transaction
    fields = ['name', 'amount', 'date', 'notes']
class Transaction_Delete(LoginRequiredMixin, DeleteView):
    model = Transaction
    success_url = reverse_lazy('transactions')






class BudgetListView(LoginRequiredMixin, ListView):
    model = Budget
class Budget_Create(LoginRequiredMixin, CreateView):
    model = Budget
    fields = ['name', 'sections']
class BudgetDetailView(LoginRequiredMixin, DetailView):
    model = Budget
    fields = ['name', 'sections']
class Budget_Update(LoginRequiredMixin, UpdateView):
    model = Budget
    fields = ['name', 'sections']
class Budget_Delete(LoginRequiredMixin, DeleteView):
    model = Budget
    success_url = reverse_lazy('budgets')
