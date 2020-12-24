from django.db import models
# Create your models here.

class Transaction(models.Model):
    name = models.CharField(max_length=64)
    amount = models.IntegerField()
    date = models.DateField()
    notes = models.TextField(blank=True)
    def __str__(self):
        return self.name

class Section(models.Model):
    name = models.CharField(max_length=64)
    transactions = models.ManyToManyField(Transaction, blank=True)
    def __str__(self):
        return self.name

class Budget(models.Model):
    name = models.CharField(max_length=64)
    section = models.ManyToManyField(Section)
    def __str__(self):
        return self.name
