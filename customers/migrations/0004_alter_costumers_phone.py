# Generated by Django 4.0.2 on 2022-02-16 16:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_alter_costumers_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costumers',
            name='phone',
            field=models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(message='Phone Number Is Not Valid', regex='^(9|(09))(((1)|(3))([0-9])|(20)|(21))(\\d{7})')], verbose_name='Phone'),
        ),
    ]
