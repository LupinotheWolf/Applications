# Generated by Django 3.1.3 on 2021-01-05 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0022_template'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='budget',
            name='amount_predicted',
        ),
    ]
