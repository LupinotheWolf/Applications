from django.contrib import admin
from .models import Transaction, Section, Budget

# Register your models here.
admin.site.register(Transaction)
admin.site.register(Section)
admin.site.register(Budget)
