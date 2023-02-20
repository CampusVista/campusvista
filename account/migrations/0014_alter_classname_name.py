# Generated by Django 4.1.7 on 2023-02-19 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0013_alter_classname_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="classname",
            name="name",
            field=models.CharField(
                choices=[
                    ("Form 1 - Blue", "Form 1 - Blue"),
                    ("Form 1 - Red", "Form 1 - Red"),
                    ("Form 1 - Green", "Form 1 - Green"),
                    ("Form 2 - Blue", "Form 2 - Blue"),
                    ("Form 2 - Red", "Form 2 - Red"),
                    ("Form 2 - Green", "Form 2 - Green"),
                ],
                default="",
                max_length=30,
            ),
        ),
    ]
