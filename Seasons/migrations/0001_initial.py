# Generated by Django 4.2.7 on 2023-11-26 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seasonName', models.CharField(max_length=10000)),
                ('seasonDescription', models.CharField(max_length=1000)),
                ('seasonDuration', models.CharField(max_length=2)),
            ],
        ),
    ]
