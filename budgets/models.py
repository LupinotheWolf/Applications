from django.db import models
from django.forms import ModelForm
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from decimal import Decimal
import datetime

now = datetime.datetime.now()
def validate_year(value):
    if value < 2000 or value > now.year+1:
        raise ValidationError(f'Please Enter a Year Between 2000 and {now.year+1}!')


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
    JAN = "January"
    FEB = "February"
    MAR = "March"
    APR = "April"
    MAY = "May"
    JUN = "June"
    JUL = "July"
    AUG = "August"
    SEP = "September"
    OCT = "October"
    NOV = "November"
    DEC = "December"

    MONTHS = (
        #(None, 'Please Select a Month'),
        (JAN, "January"),
        (FEB, "Febuary"),
        (MAR, "March"),
        (APR, "April"),
        (MAY, "May"),
        (JUN, "June"),
        (JUL, "July"),
        (AUG, "August"),
        (SEP, "September"),
        (OCT, "October"),
        (NOV, "November"),
        (DEC, "December"),
    )
    transactions = models.ManyToManyField(Transaction, blank=True)
    month = models.CharField('Month', max_length=12, choices=MONTHS, default=now.strftime('%B'), blank=False)
    year = models.IntegerField(validators=[validate_year])
    amount_predicted = models.DecimalField(max_digits=65, decimal_places=2)
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    def get_absolute_url(self):
        return reverse('budget-detail', args=[str(self.pk)])
    def __str__(self):
        return self.name

class Template(models.Model):
    name = models.CharField(max_length=64)
    budgets = models.ManyToManyField(Budget)
    all_transactions = models.ManyToManyField(Transaction, blank=True)
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Car(models.Model):
    id = models.IntegerField(primary_key=True)
    make = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    photo = models.ImageField(upload_to='media', null=True)

    class Meta:
        ordering = ["make"]
    def __str__(self):
        return self.make + self.model + ':' + str(self.photo)
