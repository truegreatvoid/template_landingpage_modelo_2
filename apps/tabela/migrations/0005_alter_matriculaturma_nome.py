# Generated by Django 5.1.4 on 2025-01-12 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabela', '0004_rename_matricula_matriculaturma'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matriculaturma',
            name='nome',
            field=models.CharField(blank=True, db_index=True, max_length=254, null=True, verbose_name='Nome'),
        ),
    ]
