# Generated by Django 3.2.9 on 2021-11-08 05:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('smsgatewayApp', '0002_statuslog'),
    ]

    operations = [
        migrations.AddField(
            model_name='statuslog',
            name='updated',
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
    ]
