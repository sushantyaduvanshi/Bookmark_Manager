# Generated by Django 2.1.5 on 2020-05-16 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0005_remove_bookmarks_check'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmarks',
            name='customer',
        ),
    ]
