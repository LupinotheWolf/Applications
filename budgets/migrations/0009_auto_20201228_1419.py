# Generated by Django 3.1.3 on 2020-12-28 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0008_auto_20201228_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
    ]
