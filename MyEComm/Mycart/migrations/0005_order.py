# Generated by Django 3.2.4 on 2021-07-11 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mycart', '0004_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_json', models.CharField(max_length=6000)),
                ('order_name', models.CharField(max_length=100)),
                ('order_email', models.CharField(max_length=100)),
                ('order_addres', models.CharField(max_length=500)),
                ('order_city', models.CharField(max_length=100)),
                ('order_zip', models.CharField(max_length=100)),
                ('order_landmark', models.CharField(max_length=200)),
                ('order_state', models.CharField(max_length=100)),
                ('order_mobile', models.IntegerField(max_length=20)),
                ('order_pincode', models.IntegerField(max_length=10)),
            ],
        ),
    ]