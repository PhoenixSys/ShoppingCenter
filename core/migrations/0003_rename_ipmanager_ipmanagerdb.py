# Generated by Django 4.0.2 on 2022-03-01 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_ipmanager'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='IpManager',
            new_name='IpManagerDb',
        ),
    ]
