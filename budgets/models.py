from django.db import models
from django.forms import ModelForm
from django.urls import reverse
from django.contrib.auth.models import User

category_list = [
    ('income', ('Income')),
    ('food', ('Food')),
    ('bills/utilities', ('Bills/Utilities')),
    ('travel', ('Travel')),
    ('amusement', ('Amusement')),
    ('misc', ('Miscellaneous')),
]


class Transaction(models.Model):
    name = models.CharField(max_length=64)
    amount = models.DecimalField(max_digits=65, decimal_places=2,)
    date = models.DateField()
    notes = models.TextField(blank=True)
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField('Transaction Type', max_length=32, choices=category_list, default='misc')
    class Metadata:
        ordering = ['date']
    def get_absolute_url(self):
        return reverse('transaction-detail', args=[str(self.pk)])
    def __str__(self):
        return self.name

class Budget(models.Model):
    transactions = models.ManyToManyField(Transaction, blank=True)
    name = models.CharField(max_length=64)
    amount_predicted = models.DecimalField(max_digits=65, decimal_places=2)
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Template(models.Model):
    name = models.CharField(max_length=64)
    budgets = models.ManyToManyField(Budget)
    all_transactions = models.ManyToManyField(Transaction, blank=True)
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
