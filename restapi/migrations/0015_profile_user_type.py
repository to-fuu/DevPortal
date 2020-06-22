# Generated by Django 2.2.11 on 2020-06-20 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0014_auto_20200620_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'normal'), (2, 'developer'), (3, 'instructor'), (4, 'organization')], default=1),
            preserve_default=False,
        ),
    ]
