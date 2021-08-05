from django.contrib import admin

# Register your models here.
from .models import Mycart,Contact,Order,OrderTracker
admin.site.register(Mycart)
admin.site.register(Contact)
admin.site.register(Order)
admin.site.register(OrderTracker)