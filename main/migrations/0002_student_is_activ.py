# Generated by Django 4.2.7 on 2023-11-14 17:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="is_activ",
            field=models.BooleanField(default=True, verbose_name="учится"),
        ),
    ]
