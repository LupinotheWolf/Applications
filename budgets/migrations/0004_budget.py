# Generated by Django 3.1.3 on 2020-12-22 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0003_auto_20201222_1326'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('section', models.ManyToManyField(to='budgets.Section')),
            ],
        ),
    ]
