# Generated by Django 2.1.5 on 2020-05-16 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0006_remove_bookmarks_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmarks',
            name='cust',
            field=models.ManyToManyField(through='bookmarks.customer_bookmark', to='bookmarks.Customer'),
        ),
    ]
