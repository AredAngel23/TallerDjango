# Generated by Django 5.1.6 on 2025-02-16 00:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AutorDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=75, verbose_name='Nombre')),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha Nacimiento')),
                ('fecha_fallecimiento', models.DateField(blank=True, null=True, verbose_name='Fecha Fallecimiento')),
                ('profesion', models.CharField(max_length=50, verbose_name='Profesion')),
                ('nacionalidad', models.CharField(max_length=50, verbose_name='Nacionalidad')),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
                'db_table': 'Autores',
            },
        ),
        migrations.CreateModel(
            name='FraseDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cita', models.TextField(max_length=400, verbose_name='Cita')),
                ('autor_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App1.autordb')),
            ],
        ),
    ]
