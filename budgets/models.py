from django.db import models
from django.forms import ModelForm
from django.urls import reverse

class Transaction(models.Model):
    name = models.CharField(max_length=64)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateField()
    notes = models.TextField(blank=True)
    class Metadata:
        ordering = ['date']
    def get_absolute_url(self):
        return reverse('transaction-detail', args=[str(self.pk)])
    def __str__(self):
        return self.name

class Section(models.Model):
    name = models.CharField(max_length=64)
    transactions = models.ManyToManyField(Transaction, blank=True)
    def __str__(self):
        return self.name

class Budget(models.Model):
    name = models.CharField(max_length=64)
    sections = models.ManyToManyField(Section)
    def __str__(self):
        return self.name

class Template(models.Model):
    name = models.CharField(max_length=64)
    budgets = models.ManyToManyField(Budget)
    all_transactions = models.ManyToManyField(Transaction)
    def __str__(self):
        return self.name
