# Generated by Django 4.1.7 on 2023-04-26 12:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Aadhar',
            field=models.CharField(max_length=30, validators=[django.core.validators.MaxLengthValidator(12), django.core.validators.MinLengthValidator(12), django.core.validators.RegexValidator('\\d{12}')]),
        ),
    ]
