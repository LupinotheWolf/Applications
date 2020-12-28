from django.forms import ModelForm
from budgets.models import Transaction

class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['name', 'amount', 'date', 'notes']
