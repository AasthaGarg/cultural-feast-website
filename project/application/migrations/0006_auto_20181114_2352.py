# Generated by Django 2.0.9 on 2018-11-14 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_auto_20181114_2342'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='contact',
            new_name='contact_no',
        ),
    ]
