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
from django.db.models import Sum

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

@login_required
def template(request):
    try:
        template = Template.objects.get(account=request.user)
    except Template.DoesNotExist:
        template = None
    if template is not None:
        pre_bills = Pre_Bills.objects.filter(account=request.user).aggregate(Sum('amount'))
        bills_list = Pre_Bills.objects.filter(account=request.user)
        pre_all = template.pre_food + pre_bills['amount__sum'] + template.pre_travel + template.pre_amusement
        remaining = template.pre_income - pre_all
        return render(request, "budgets/template-view.html", {
            'template': template,
            'pre_all': pre_all,
            'remaining': remaining,
            'pre_bills': pre_bills['amount__sum'],
            'bills_list': bills_list,
        })
    else:
        return render(request, "budgets/template-create.html", {
            'message': 'You have no template to view! Please use the form to creat a new template!'
        })

@login_required
def template_edit(request):
    #be sure to add a form here!!
    check = Template.objects.get(account=request.user)
    if check is not None:
        template = Template.objects.get(account=request.user)
        return render(request, "budgets/template-edit.html", {
            'template': template,
        })
    else:
        return render(request, "budgets/template-create.html", {
            #'form': form,
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

class TemplateCreate(LoginRequiredMixin, CreateView):
    model = Template
    fields = ['pre_income', 'pre_food', 'pre_travel', 'pre_amusement']
    def form_valid(self, form):
        form.instance.account = self.request.user
        return super().form_valid(form)

class BudgetListView(LoginRequiredMixin, ListView):
    model = Budget
    def get_queryset(self):
        return Budget.objects.filter(account=self.request.user)
class Budget_Create(LoginRequiredMixin, CreateView):
    model = Budget
    fields = ['month', 'year', 'transactions', 'amount_predicted']
    def form_valid(self, form):
        form.instance.account = self.request.user
        return super().form_valid(form)
class BudgetDetailView(LoginRequiredMixin, DetailView):
    model = Budget
    fields = ['name', 'transactions', 'amount_predicted']
class Budget_Update(LoginRequiredMixin, UpdateView):
    model = Budget
    fields = ['name', 'sections']
class Budget_Delete(LoginRequiredMixin, DeleteView):
    model = Budget
    success_url = reverse_lazy('budgets')
