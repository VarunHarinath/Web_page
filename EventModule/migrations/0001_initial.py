# Generated by Django 4.2.7 on 2023-11-05 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventTitle', models.CharField(max_length=100000)),
                ('eventAddress', models.CharField(max_length=100000)),
                ('eventDescription', models.TextField()),
                ('eventDuration', models.TimeField()),
                ('eventLocation', models.CharField(max_length=100000)),
                ('eventDate', models.DateField()),
            ],
        ),
    ]
