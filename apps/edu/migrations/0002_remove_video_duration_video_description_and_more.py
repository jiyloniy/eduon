# Generated by Django 5.0.2 on 2024-07-14 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='duration',
        ),
        migrations.AddField(
            model_name='video',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='embed_link',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='play_link',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
