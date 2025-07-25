# Generated by Django 5.2.4 on 2025-07-22 10:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('value', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='category_type',
        ),
        migrations.RemoveField(
            model_name='event',
            name='name',
        ),
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='title',
            field=models.CharField(default=datetime.datetime(2025, 7, 22, 10, 3, 32, 100274, tzinfo=datetime.timezone.utc), max_length=200),
            preserve_default=False,
        ),
    ]
