# Generated by Django 2.0.5 on 2018-05-26 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bucketlist',
            new_name='Shoppinglist',
        ),
    ]