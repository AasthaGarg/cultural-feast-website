# Generated by Django 2.0.9 on 2018-11-16 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0009_querry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='querry',
            old_name='querry',
            new_name='query',
        ),
    ]
