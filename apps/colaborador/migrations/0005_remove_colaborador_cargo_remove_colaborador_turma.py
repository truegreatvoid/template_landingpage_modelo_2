# Generated by Django 5.1.4 on 2025-01-16 02:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colaborador', '0004_alter_colaborador_turma'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='colaborador',
            name='cargo',
        ),
        migrations.RemoveField(
            model_name='colaborador',
            name='turma',
        ),
    ]
