# Generated by Django 4.1.7 on 2023-02-24 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("acct", "0007_alter_student_parent"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="parent",
        ),
    ]
