# Generated by Django 2.2.20 on 2021-08-13 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0023_auto_20210813_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='photo',
            field=models.FileField(null=True, upload_to='images/', verbose_name=''),
        ),
    ]
