from django import forms
from zamowienia.models import Order, OrderId, Client
import datetime

class NameForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('Order_Id', 'Item_Name', 'Catalog_Id', 'Item_Cost', 'Client_Name')

class neworder(forms.ModelForm):

    class Meta:
        model = OrderId
        fields = ('OrderId', 'Order_Data')

class neworderitem(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('Order_Id', 'Item_Name', 'Catalog_Id', 'Item_Cost', 'Client_Name')

class newclient(forms.ModelForm):

    class Meta:
        model = Client
        fields = ('Name',)

