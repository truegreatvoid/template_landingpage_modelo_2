# Generated by Django 5.1.4 on 2025-01-12 22:34

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colaborador', '0004_alter_colaborador_turma'),
        ('tabela', '0003_matricula'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Matricula',
            new_name='MatriculaTurma',
        ),
    ]
