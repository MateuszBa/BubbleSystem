from django import forms
from zamowienia.models import Order

class NameForm(forms.ModelForm):
    Item_Name = forms.CharField(label='Item Name', max_length=100)
    Catalog_Id = forms.IntegerField(label='Catalog_Id')
    Client_Id = forms.IntegerField(label='Client_Id')

    class Meta:
        model = Order
        fields = ('Item_Name', 'Catalog_Id', 'Client_Id',)