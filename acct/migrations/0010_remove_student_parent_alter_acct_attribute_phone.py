# Generated by Django 4.1.7 on 2023-02-25 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("acct", "0009_student_parent"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="parent",
        ),
        migrations.AlterField(
            model_name="acct_attribute",
            name="phone",
            field=models.CharField(max_length=15),
        ),
    ]
