# Generated by Django 2.0.9 on 2018-11-20 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0015_auto_20181120_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='reg',
            field=models.IntegerField(),
        ),
    ]
