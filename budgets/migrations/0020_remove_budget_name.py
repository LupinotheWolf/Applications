# Generated by Django 3.1.3 on 2021-01-05 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0019_auto_20210105_1127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='budget',
            name='name',
        ),
    ]
