from django.forms import ModelForm
from budgets.models import *

class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['name', 'amount', 'date', 'notes']
