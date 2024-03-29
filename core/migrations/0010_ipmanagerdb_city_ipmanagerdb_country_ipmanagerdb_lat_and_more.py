# Generated by Django 4.0.2 on 2022-03-26 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_remove_ipmanagerdb_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ipmanagerdb',
            name='city',
            field=models.CharField(default='Iran', max_length=32, verbose_name='City'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ipmanagerdb',
            name='country',
            field=models.CharField(default='Iran', max_length=32, verbose_name='Country'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ipmanagerdb',
            name='lat',
            field=models.CharField(default='Iran', max_length=32, verbose_name='Lat'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ipmanagerdb',
            name='lon',
            field=models.CharField(default='Iran', max_length=32, verbose_name='Lon'),
            preserve_default=False,
        ),
    ]
