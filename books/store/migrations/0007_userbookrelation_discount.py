# Generated by Django 3.2 on 2021-05-04 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_userbookrelation_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbookrelation',
            name='discount',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
