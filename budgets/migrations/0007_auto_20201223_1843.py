# Generated by Django 3.1.3 on 2020-12-23 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0006_section_transactions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='notes',
            field=models.TextField(blank=True),
        ),
    ]
