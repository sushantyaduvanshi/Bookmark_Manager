# Generated by Django 2.1.5 on 2020-05-16 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0003_auto_20200516_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmarks',
            name='check',
            field=models.CharField(default='1', max_length=10),
        ),
    ]