# Generated by Django 3.2.4 on 2024-12-18 18:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='content',
            field=models.TextField(validators=[django.core.validators.MaxLengthValidator(500)]),
        ),
    ]
