# Generated by Django 4.0.2 on 2022-03-01 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_ipmanagerdb_access_alter_ipmanagerdb_ip_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ipmanagerdb',
            name='created',
        ),
        migrations.RemoveField(
            model_name='ipmanagerdb',
            name='delete_timestamp',
        ),
        migrations.RemoveField(
            model_name='ipmanagerdb',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='ipmanagerdb',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='ipmanagerdb',
            name='is_deleted',
        ),
        migrations.RemoveField(
            model_name='ipmanagerdb',
            name='last_updated',
        ),
    ]
