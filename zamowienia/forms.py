from django import forms
from zamowienia.models import Order, OrderId

class NameForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('Order_Id','Item_Name', 'Catalog_Id','Item_Cost' ,'Client_Name')

class delete(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('Item_Name',)