from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import NameForm, delete
from django.db.models import Sum
from django.urls import reverse

from .models import Order, OrderId

def detail(request, Order_Id):
    items = Order.objects.filter(Order_Id__OrderId=Order_Id)
    suma = Order.objects.values('Order_Id').filter(Order_Id__OrderId=Order_Id).annotate(Sum('Item_Cost'))
    return render(request, 'zamowienia/detail.html', {'items': items, 'suma': suma[0]})

def index(request):
    ordernumbers = OrderId.objects.order_by('OrderId')[:5]
    context = {'orders': ordernumbers}
    return render(request, 'zamowienia/index.html', context)


def addorder(request):
    return render(request, 'zamowienia/addorder.html')

def additem(request, Order_Id):
    items = Order.objects.filter(Order_Id__OrderId=Order_Id)
    suma = Order.objects.values('Order_Id').filter(Order_Id__OrderId=Order_Id).annotate(Sum('Item_Cost'))
    var1 = OrderId.objects.filter(OrderId = Order_Id)
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.Order_Id = var1[0]
            form.save()
            return render(request, 'zamowienia/detail.html', {'items': items, 'suma': suma[0]})
    else:
        form = NameForm()

    return render(request, 'zamowienia/additem.html', {'form': form})

def usun(request, Order_Id):
    item = Order.objects.filter(Order_Id__OrderId=Order_Id)
    deletes = delete(request.POST)
    return render(request, 'zamowienia/delete.html', {'deletes': deletes})

def Clients(request):
    List_of_CLients = Order.objects.values('Client_Name__Name').annotate(Sum('Client_Name'))
    Lista = {'List_of_CLients': List_of_CLients}
    return render(request, 'zamowienia/clients.html', Lista)

def Client_detail(request, Client_Name):
    ords = Order.objects.values('Order_Id').annotate(Sum('Client_Name')).filter(Client_Name__Name = Client_Name)
    return render(request, 'zamowienia/client_detail.html', {'ords': ords})

def Client_order_detail(request, Order_Id, Client_Name):
    items = Order.objects.annotate(Sum('Client_Name')).filter(Order_Id__OrderId=Order_Id, Client_Name__Name = Client_Name)
    suma = Order.objects.values('Order_Id').filter(Client_Name__Name = Client_Name, Order_Id__OrderId=Order_Id).annotate(Sum('Item_Cost'))
    return render(request, 'zamowienia/client_order_detail.html', {'items': items, 'suma': suma[0]})

def orders(request):
    ordernumbers = OrderId.objects.order_by('OrderId')[:5]
    context = {'orders': ordernumbers}
    return render(request, 'zamowienia/orders.html', context)