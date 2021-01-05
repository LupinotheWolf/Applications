# Generated by Django 3.1.3 on 2021-01-05 10:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0017_budget_month'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget',
            name='year',
            field=models.IntegerField(default=2020, validators=[django.core.validators.MinValueValidator(2000), django.core.validators.MaxValueValidator(2021)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='budget',
            name='month',
            field=models.CharField(choices=[(None, 'Please Select a Month'), ('January', 'January'), ('February', 'Febuary'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], max_length=12, verbose_name='Month'),
        ),
    ]