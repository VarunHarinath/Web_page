# Generated by Django 4.2.7 on 2023-11-26 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seasons', '0004_season_seasondate_season_seasonlocation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='season',
            name='seasonSpeaker',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]