# Generated by Django 5.1.4 on 2025-01-29 03:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_remove_saverecipes_recipes_saverecipes_recipes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saverecipes',
            name='recipes',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='saved_recipes', to='app.recipe'),
        ),
    ]
