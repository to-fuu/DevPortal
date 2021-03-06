# Generated by Django 2.2.11 on 2020-06-21 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0018_forum_forumthread_threadpost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='forumthread',
            old_name='project',
            new_name='forum',
        ),
        migrations.RenameField(
            model_name='threadpost',
            old_name='project',
            new_name='thred',
        ),
        migrations.AddField(
            model_name='threadpost',
            name='title',
            field=models.CharField(default='title', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='forumthread',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
