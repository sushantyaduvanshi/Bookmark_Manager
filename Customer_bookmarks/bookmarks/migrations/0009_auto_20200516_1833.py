# Generated by Django 2.1.5 on 2020-05-16 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0008_auto_20200516_1818'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookmarks',
            old_name='data',
            new_name='date',
        ),
    ]
