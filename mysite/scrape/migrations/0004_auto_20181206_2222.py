# Generated by Django 2.1.3 on 2018-12-07 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrape', '0003_url_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='tag',
            field=models.CharField(default='div', max_length=7),
        ),
    ]
