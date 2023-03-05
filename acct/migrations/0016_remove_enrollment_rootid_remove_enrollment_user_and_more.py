# Generated by Django 4.1.7 on 2023-03-02 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("acct", "0015_remove_classname_teacher_id_classname_class_teacher"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="enrollment",
            name="rootid",
        ),
        migrations.RemoveField(
            model_name="enrollment",
            name="user",
        ),
        migrations.AddField(
            model_name="enrollment",
            name="student",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="enrollments",
                to="acct.student",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="enrollment",
            name="staff_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="acct.student"
            ),
        ),
    ]