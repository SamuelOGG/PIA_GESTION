# Generated by Django 5.0.4 on 2024-04-22 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='TiempoPreparación',
        ),
    ]
