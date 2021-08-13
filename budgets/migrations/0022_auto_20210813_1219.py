# Generated by Django 2.2.20 on 2021-08-13 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0021_auto_20210707_1225'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=64)),
                ('model', models.CharField(max_length=64)),
                ('photo', models.ImageField(upload_to='cars')),
            ],
        ),
        migrations.AlterField(
            model_name='budget',
            name='month',
            field=models.CharField(choices=[('January', 'January'), ('February', 'Febuary'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], default='August', max_length=12, verbose_name='Month'),
        ),
    ]
