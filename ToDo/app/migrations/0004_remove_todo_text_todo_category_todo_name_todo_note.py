# Generated by Django 5.1 on 2024-08-26 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_attechedfile_todo_attached_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='text',
        ),
        migrations.AddField(
            model_name='todo',
            name='Category',
            field=models.TextField(default='Uncategorized', max_length=100),
        ),
        migrations.AddField(
            model_name='todo',
            name='Name',
            field=models.TextField(default='Unnamed', max_length=100),
        ),
        migrations.AddField(
            model_name='todo',
            name='Note',
            field=models.TextField(default='No notes', max_length=200),
        ),
    ]
