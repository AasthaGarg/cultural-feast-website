# Generated by Django 2.0.9 on 2018-11-20 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0010_auto_20181116_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='reg',
            field=models.ForeignKey(default='', on_delete='CASCADE', to='application.Reg'),
        ),
    ]
