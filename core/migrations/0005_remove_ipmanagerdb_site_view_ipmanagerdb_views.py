# Generated by Django 4.0.2 on 2022-03-01 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_ipmanagerdb_site_view'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ipmanagerdb',
            name='site_view',
        ),
        migrations.AddField(
            model_name='ipmanagerdb',
            name='views',
            field=models.IntegerField(default=1),
        ),
    ]
