# Generated by Django 3.1.3 on 2021-05-11 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_album_cover_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='cover_photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/images'),
        ),
    ]