# Generated by Django 3.2.4 on 2021-06-30 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mycart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mycart',
            name='category',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='mycart',
            name='image',
            field=models.ImageField(default='', upload_to='Mycart/images'),
        ),
        migrations.AddField(
            model_name='mycart',
            name='price',
            field=models.ImageField(default=0, upload_to=''),
        ),
        migrations.AddField(
            model_name='mycart',
            name='subcategory',
            field=models.CharField(default='', max_length=50),
        ),
    ]
