# Generated by Django 3.2.4 on 2021-07-11 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mycart', '0006_auto_20210712_0131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_mobile',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_pincode',
            field=models.IntegerField(default=''),
        ),
    ]
