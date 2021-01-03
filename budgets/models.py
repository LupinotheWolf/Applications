from django.db import models
from django.forms import ModelForm
from django.urls import reverse
from django.contrib.auth.models import User

from decimal import Decimal


class Transaction(models.Model):
    I = "Income"
    F = "Food"
    B = "Bills/Utilities"
    T = "Travel"
    A = "Amusement"
    M = "Miscellaneous"
    CHOICES = (
        (I, "Income"),
        (F, "Food"),
        (B, "Bills/Utilities"),
        (T, "Travel"),
        (A, "Amusement"),
        (M, "Miscellaneous"),
    )
    name = models.CharField(max_length=64)
    amount = models.DecimalField(max_digits=65, decimal_places=2,)
    date = models.DateField()
    notes = models.TextField(blank=True)
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField('Category', max_length=32, choices=CHOICES, default=I, blank=False)
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
    def amount_remaining(self, amount_pre, sum):
        amount_pre = Decimal(amount_pre)
        sum = Decimal(sum)
        return amount_pre - sum
    def __str__(self):
        return self.name

class Template(models.Model):
    name = models.CharField(max_length=64)
    budgets = models.ManyToManyField(Budget)
    all_transactions = models.ManyToManyField(Transaction, blank=True)
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
