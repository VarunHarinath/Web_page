# Generated by Django 4.2.7 on 2023-11-26 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seasons', '0002_season_seasonimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='season',
            name='seasonContactPhoneNumber_1',
            field=models.IntegerField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='season',
            name='seasonContactPhoneNumber_2',
            field=models.IntegerField(max_length=10, null=True),
        ),
    ]