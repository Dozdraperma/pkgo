# Generated by Django 3.2.5 on 2021-07-13 14:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('pokemon_base', '0003_auto_20210713_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='evolves_from',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING,
                                    related_name='evolves_to', to='pokemon_base.pokemon'),
        ),
    ]
