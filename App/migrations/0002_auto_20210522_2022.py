# Generated by Django 3.1.7 on 2021-05-22 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='audio_link',
        ),
        migrations.RemoveField(
            model_name='song',
            name='duration',
        ),
    ]
