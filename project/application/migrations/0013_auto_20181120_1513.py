# Generated by Django 2.0.9 on 2018-11-20 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0012_auto_20181120_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='reg',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Reg'),
        ),
    ]
