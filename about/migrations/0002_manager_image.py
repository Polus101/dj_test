# Generated by Django 4.1.4 on 2025-05-26 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='image',
            field=models.ImageField(default='aboba', upload_to='about/'),
        ),
    ]
