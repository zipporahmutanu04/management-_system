# Generated by Django 5.2.4 on 2025-07-22 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('value', '0002_remove_event_category_type_remove_event_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='capacity',
            field=models.IntegerField(default=30),
        ),
    ]
