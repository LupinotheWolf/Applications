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

# class Bills(models.Model):
#     account = models.ForeignKey(User, on_delete=models.CASCADE)





class Template(models.Model):
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    pre_income = models.DecimalField(max_digits=65, decimal_places=2,)
    pre_food = models.DecimalField(max_digits=65, decimal_places=2,)
    pre_bills = models.DecimalField(max_digits=65, decimal_places=2,)
    pre_travel = models.DecimalField(max_digits=65, decimal_places=2,)
    pre_amusement = models.DecimalField(max_digits=65, decimal_places=2,)
    def __str__(self):
        return 'Template'




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
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    def get_absolute_url(self):
        return reverse('budget-detail', args=[str(self.pk)])
    def __str__(self):
        return f"{self.month} {self.year}"
