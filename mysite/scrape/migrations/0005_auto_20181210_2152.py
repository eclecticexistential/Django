# Generated by Django 2.1.3 on 2018-12-11 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrape', '0004_auto_20181206_2222'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='class_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='url',
            name='id_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]