# Generated by Django 3.0.4 on 2020-03-31 01:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0002_list_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='user',
        ),
    ]
