# Generated by Django 5.1.6 on 2025-02-17 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0003_rename_profesion_profesiondb'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profesiondb',
            options={'verbose_name': 'Profesión', 'verbose_name_plural': 'Profesiones'},
        ),
        migrations.AlterModelTable(
            name='frasedb',
            table='Frases',
        ),
        migrations.AlterModelTable(
            name='profesiondb',
            table='Profesiones',
        ),
    ]
