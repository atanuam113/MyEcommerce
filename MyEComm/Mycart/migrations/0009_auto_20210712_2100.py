# Generated by Django 3.2.4 on 2021-07-12 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mycart', '0008_auto_20210712_0134'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order_addres',
            new_name='addres',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='order_city',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='order_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='order_landmark',
            new_name='landmark',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='order_mobile',
            new_name='mobile',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='order_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='order_pincode',
            new_name='pincode',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='order_state',
            new_name='state',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='order_zip',
            new_name='zip',
        ),
    ]