# Generated by Django 3.0.4 on 2020-04-12 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0010_auto_20200412_0314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='priority',
            field=models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], default='Medium', max_length=10),
        ),
    ]
