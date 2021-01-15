# Generated by Django 3.0.3 on 2021-01-15 15:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('ST', 'Shirt'), ('SW', 'Sport Wear'), ('ST', 'Shirt')], default=datetime.datetime(2021, 1, 15, 15, 49, 45, 828236, tzinfo=utc), max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('PR', 'Primary'), ('SC', 'Secondary'), ('DR', 'Danger')], default=django.utils.timezone.now, max_length=2),
            preserve_default=False,
        ),
    ]
