# Generated by Django 2.2.20 on 2021-08-13 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0022_auto_20210813_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
