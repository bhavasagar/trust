# Generated by Django 2.2.10 on 2021-01-19 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_trustteammember_designation'),
    ]

    operations = [
        migrations.CreateModel(
            name='YouTubeVideos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.CharField(max_length=20)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
