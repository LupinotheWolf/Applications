# Generated by Django 3.1.3 on 2021-05-11 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20210511_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='cover_photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
