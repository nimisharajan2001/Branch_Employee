# Generated by Django 4.0.2 on 2022-03-14 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0002_auto_20220305_1311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project_taskassign',
            name='employee_files',
        ),
        migrations.AddField(
            model_name='project_taskassign',
            name='json_screenshot',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
