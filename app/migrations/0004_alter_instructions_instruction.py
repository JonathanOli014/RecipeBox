# Generated by Django 5.1.4 on 2024-12-29 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_recipe_instructions_instructions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructions',
            name='instruction',
            field=models.TextField(),
        ),
    ]