from django.urls import path

from . import views

app_name = 'zamowienia'
urlpatterns = [
    path('indeks', views.index, name='index'),
    path('<int:OrderId>/', views.detail, name='detail'),
    path('<int:OrderId>/additem', views.additem, name='additem'),
    path('addorder/', views.addorder, name='addorder'),
    path('clients/', views.Clients, name='clients'),
    path('clients/<str:Client_Name>/', views.Client_detail, name='Client_detail'),
    path('clients/<str:Client_Name>/<int:Order_Id>', views.Client_order_detail, name='client_order_detail'),
    path('orders', views.orders, name='orders'),
    path('clients/<str:Client_Name>/<int:var>/Client_new/', views.Client_new, name='Client_new'),
    path('about', views.about, name='about'),
    path('clients/newclient', views.newclients, name='newclient'),
]