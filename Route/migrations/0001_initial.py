# Generated by Django 2.2.1 on 2020-04-02 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='routes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('routetag', models.CharField(max_length=20)),
                ('route', models.CharField(max_length=50)),
                ('nexthop', models.CharField(max_length=20)),
            ],
        ),
    ]