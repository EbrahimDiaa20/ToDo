# Generated by Django 5.1 on 2024-08-24 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_todo_attechedfile_alter_todo_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='AttechedFile',
            new_name='attached_file',
        ),
    ]