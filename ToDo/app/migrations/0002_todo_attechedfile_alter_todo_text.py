# Generated by Django 5.1 on 2024-08-24 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='AttechedFile',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='text',
            field=models.TextField(max_length=500),
        ),
    ]
