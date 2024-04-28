# Generated by Django 5.0.4 on 2024-04-28 07:34

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notesBoard", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="note",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="note",
            name="modified_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
