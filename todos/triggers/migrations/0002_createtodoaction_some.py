# Generated by Django 4.1.7 on 2023-02-28 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todos_triggers", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="createtodoaction",
            name="some",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]