# Generated by Django 4.1.7 on 2023-02-19 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0007_staff"),
    ]

    operations = [
        migrations.AlterField(
            model_name="staff",
            name="position",
            field=models.CharField(
                choices=[
                    ("Headmaster", "Headmaster"),
                    ("Teacher", "Teacher"),
                    ("Administrator", "Administrator"),
                ],
                max_length=20,
            ),
        ),
    ]
