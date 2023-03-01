# Generated by Django 4.1.7 on 2023-03-01 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("triggers", "0003_event_delay"),
        ("todos_triggers", "0002_createtodoaction_some"),
    ]

    operations = [
        migrations.CreateModel(
            name="SendEmailAction",
            fields=[
                (
                    "action_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="triggers.action",
                    ),
                ),
                (
                    "email_message",
                    models.TextField(blank=True, verbose_name="email message"),
                ),
            ],
            options={
                "verbose_name": "send email action",
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("triggers.action",),
        ),
        migrations.DeleteModel(
            name="CreateTodoAction",
        ),
    ]