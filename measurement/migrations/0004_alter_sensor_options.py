# Generated by Django 4.2.2 on 2023-06-17 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0003_alter_sensor_options_remove_measurement_temp_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sensor',
            options={'ordering': ['id']},
        ),
    ]