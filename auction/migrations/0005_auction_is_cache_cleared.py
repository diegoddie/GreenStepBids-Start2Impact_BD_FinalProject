# Generated by Django 4.2.4 on 2023-08-27 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0004_auction_ethereum_tx_auction_is_ended'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='is_cache_cleared',
            field=models.BooleanField(default=False),
        ),
    ]
