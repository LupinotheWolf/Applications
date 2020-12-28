from django import forms
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import *
from .forms import *

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "budgets/login.html",)
    else:
        return render(request, "budgets/index.html", {
            'budgets': Transaction.objects.all(),
            'templates': Template.objects.all(),
        })

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'budgets/login.html', {
                'message': 'Invalid Credentials!'
            })
    else:
        return render(request, 'budgets/login.html')

def logout_view(request):
    logout(request)
    return render(request, 'budgets/login.html', {
        'message': 'You have Logged Out successfuly!',
        'logout_msg': 'Click Here to Login Again',
    })

def overview(request):
    return render(request, "budgets/overview.html", {
        'transactions': Transaction.objects.all(),
    })

def transaction(request, trans_id):
    trans_request = Transaction.objects.get(id=trans_id)
    return render(request, "budgets/transaction.html", {
        'transaction': trans_request,
    })

def transaction_detailview(request):
    return render(request, "transaction-detailview.html")


class TransactionListView(ListView):
    model = Transaction
class TransactionDetailView(DetailView):
    model = Transaction
    fields = ['name', 'amount', 'date', 'notes']
class Transaction_Create(CreateView):
    model = Transaction
    fields = ['name', 'amount', 'date', 'notes']
class Transaction_Update(UpdateView):
    model = Transaction
    fields = ['name', 'amount', 'date', 'notes']
class Transaction_Delete(DeleteView):
    model = Transaction
    success_url = reverse_lazy('transactions')
