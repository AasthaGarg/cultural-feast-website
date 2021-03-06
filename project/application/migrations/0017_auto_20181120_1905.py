# Generated by Django 2.0.9 on 2018-11-20 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0016_auto_20181120_1831'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Reg',
        ),
        migrations.RemoveField(
            model_name='event',
            name='reg',
        ),
        migrations.AddField(
            model_name='event',
            name='college',
            field=models.CharField(default='BCET Gurdaspur', max_length=500),
        ),
        migrations.AddField(
            model_name='event',
            name='contact_no',
            field=models.CharField(default='', max_length=20, unique=True),
        ),
        migrations.AddField(
            model_name='event',
            name='course',
            field=models.CharField(default='Btech', max_length=100),
        ),
        migrations.AddField(
            model_name='event',
            name='email',
            field=models.EmailField(default='', max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='event',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='event',
            name='password',
            field=models.CharField(default='', max_length=20),
        ),
    ]
