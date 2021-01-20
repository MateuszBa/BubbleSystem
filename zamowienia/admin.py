from django.contrib import admin

from .models import Order, OrderId, Client

admin.site.register(Order)
admin.site.register(OrderId)
admin.site.register(Client)


