# Generated by Django 2.2.10 on 2021-01-19 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_youtubevideos'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='YouTubeVideos',
            new_name='YouTubeVideo',
        ),
    ]