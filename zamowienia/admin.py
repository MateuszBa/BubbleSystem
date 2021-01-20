from django.contrib import admin

from .models import Order, OrderId

admin.site.register(Order)
admin.site.register(OrderId)

