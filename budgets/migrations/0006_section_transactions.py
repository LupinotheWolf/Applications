# Generated by Django 3.1.3 on 2020-12-23 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0005_remove_section_transactions'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='transactions',
            field=models.ManyToManyField(blank=True, to='budgets.Transaction'),
        ),
    ]
