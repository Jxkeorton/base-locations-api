# Generated by Django 3.2.4 on 2024-11-06 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0004_alter_location_rock_drop'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='total_height',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]