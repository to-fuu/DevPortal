# Generated by Django 2.2.11 on 2020-05-18 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0006_project_repo'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='restapi.Project'),
        ),
    ]
