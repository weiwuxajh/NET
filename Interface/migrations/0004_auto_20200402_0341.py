# Generated by Django 2.2.1 on 2020-04-02 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Interface', '0003_devicelist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='devicelist',
            old_name='device_type',
            new_name='devicetype',
        ),
    ]
