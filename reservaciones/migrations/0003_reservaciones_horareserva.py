# Generated by Django 5.0.4 on 2024-04-30 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservaciones', '0002_rename_telefono_reservaciones_telefono_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservaciones',
            name='HoraReserva',
            field=models.TimeField(null=True),
        ),
    ]
