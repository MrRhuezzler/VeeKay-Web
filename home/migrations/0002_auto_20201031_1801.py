# Generated by Django 3.1.2 on 2020-10-31 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='genre',
            field=models.CharField(default='Pop', max_length=100),
        ),
        migrations.AddField(
            model_name='album',
            name='release_year',
            field=models.CharField(default='2020', max_length=100),
        ),
        migrations.AddField(
            model_name='single',
            name='genre',
            field=models.CharField(default='Pop', max_length=100),
        ),
        migrations.AddField(
            model_name='single',
            name='release_year',
            field=models.CharField(default='2020', max_length=100),
        ),
    ]