# Generated by Django 5.1.4 on 2025-01-28 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_rename_user_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
