# Generated by Django 5.2 on 2025-05-03 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TourList', '0003_tour_is_active_tour_view_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]
