# Generated by Django 4.2.7 on 2023-11-05 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventModule', '0002_projectpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectpost',
            name='projectMemebers',
            field=models.IntegerField(),
        ),
    ]