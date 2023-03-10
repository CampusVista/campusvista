# Generated by Django 4.1.7 on 2023-03-03 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("acct", "0016_remove_enrollment_rootid_remove_enrollment_user_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="transcript",
            old_name="student_id",
            new_name="student",
        ),
        migrations.AlterField(
            model_name="enrollment",
            name="staff_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="acct.staff"
            ),
        ),
    ]
