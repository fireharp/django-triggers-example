# Generated by Django 4.1.7 on 2023-03-01 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("triggers", "0003_event_delay"),
        ("todos_triggers", "0003_sendemailaction_delete_createtodoaction"),
    ]

    operations = [
        migrations.CreateModel(
            name="UnfinishedTodosCountCondition",
            fields=[
                (
                    "condition_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="triggers.condition",
                    ),
                ),
                (
                    "lookup",
                    models.CharField(
                        choices=[("exact", "=="), ("gte", ">=")],
                        default="exact",
                        max_length=8,
                        verbose_name="lookup",
                    ),
                ),
                ("value", models.PositiveIntegerField(verbose_name="value")),
            ],
            options={
                "verbose_name": "unfinished todos count condition",
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("triggers.condition",),
        ),
        migrations.RenameModel(
            old_name="TodoIsCompletedEvent",
            new_name="TodoIsFinishedEvent",
        ),
        migrations.AlterModelOptions(
            name="todoisfinishedevent",
            options={
                "base_manager_name": "objects",
                "verbose_name": "todo is finished event",
            },
        ),
        migrations.DeleteModel(
            name="TodoIsImportantCondition",
        ),
    ]