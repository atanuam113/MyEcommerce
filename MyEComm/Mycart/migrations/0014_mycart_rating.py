# Generated by Django 3.2.4 on 2021-09-27 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mycart', '0013_auto_20210926_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='mycart',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
