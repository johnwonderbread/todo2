# Generated by Django 3.0.4 on 2020-04-11 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0006_auto_20200331_0136'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='list',
            name='title',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='todo_list.ListName'),
        ),
    ]
