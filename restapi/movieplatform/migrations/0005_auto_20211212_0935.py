# Generated by Django 3.2 on 2021-12-12 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieplatform', '0004_auto_20211212_0755'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='avg_ratting',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='number_ratting',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
