from django.db import models

# Create your models here.

# Product details data
class Mycart(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50,default="")
    subcategory = models.CharField(max_length=50,default="")

    brand = models.CharField(max_length=50,default="")
    avl_colour = models.CharField(max_length=50,default="")
    specifation = models.CharField(max_length=50,default="")
    price = models.IntegerField(default=0)
    rating = models.FloatField(default=0)
    image = models.ImageField(upload_to="Mycart/images",default="")
    sub_image11 = models.ImageField(upload_to="Mycart/images",default="")
    sub_image12 = models.ImageField(upload_to="Mycart/images",default="")
    sub_image13 = models.ImageField(upload_to="Mycart/images",default="")
    sub_image21 = models.ImageField(upload_to="Mycart/images",default="")
    sub_image22 = models.ImageField(upload_to="Mycart/images",default="")
    sub_image23 = models.ImageField(upload_to="Mycart/images",default="")
    sub_image31 = models.ImageField(upload_to="Mycart/images",default="")
    sub_image32 = models.ImageField(upload_to="Mycart/images",default="")
    sub_image33 = models.ImageField(upload_to="Mycart/images",default="")
    desc = models.CharField(max_length=400)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.product_name

# Contact us page data
class Contact(models.Model):

    message_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)
    email = models.CharField(max_length=80,default="")
    message = models.CharField(max_length=500,default="")
    # message_date = models.DateTimeField()

    def __str__(self):
        return self.name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_json = models.CharField(max_length=6000)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    landmark = models.CharField(max_length=200)
    state = models.CharField(max_length=100)
    mobile = models.IntegerField(default=0)
    pincode = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class OrderTracker(models.Model):
    Track_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default='')
    Track_desc = models.CharField(max_length=4000)
    Track_time = models.DateField(auto_now=True)

    def __str__(self):
        return self.Track_desc[0:10] + "..."
