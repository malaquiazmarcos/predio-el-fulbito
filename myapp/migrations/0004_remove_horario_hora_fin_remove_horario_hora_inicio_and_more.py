# Generated by Django 5.1.2 on 2024-11-03 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_datospersona'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='horario',
            name='hora_fin',
        ),
        migrations.RemoveField(
            model_name='horario',
            name='hora_inicio',
        ),
        migrations.AddField(
            model_name='horario',
            name='horarios',
            field=models.TextField(default='', max_length=50),
        ),
    ]
