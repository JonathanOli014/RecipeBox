# Generated by Django 5.1.4 on 2025-01-01 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_instructions_instruction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='updatedAt',
        ),
    ]
