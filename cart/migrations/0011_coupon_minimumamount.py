# Generated by Django 4.2.2 on 2023-08-11 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0010_cart_razor_pay_order_id_cart_razor_pay_payment_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='minimumamount',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
