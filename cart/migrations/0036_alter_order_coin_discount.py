# Generated by Django 4.2.3 on 2023-09-04 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0035_order_coin_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='coin_discount',
            field=models.IntegerField(default=0),
        ),
    ]
