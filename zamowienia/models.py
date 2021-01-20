from django.db import models

class OrderId(models.Model):
    OrderId = models.IntegerField(default=0)
    Order_Data = models.DateTimeField('Create Date')

    def __str__(self):
        return str(self.OrderId)

class Order(models.Model):
    Order_Id = models.ForeignKey(OrderId, on_delete=models.CASCADE)
    Item_Name = models.CharField(max_length=200)
    Catalog_Id = models.IntegerField(default=0)
    Client_Name = models.CharField(max_length=200)
    Item_Cost = models.IntegerField(default=0)

    def __str__(self):
        return self.Item_Name

class Client(models.Model):
    Name = models.CharField(max_length=200)
    Surname = models.CharField(max_length=200)


