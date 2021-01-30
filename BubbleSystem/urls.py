from django.contrib import admin
from django.urls import path
from zamowienia import views

app_name = 'zamowienia'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('<int:Order_Id>/', views.detail, name='detail'),
    path('<int:Order_Id>/additem', views.additem, name='additem'),
    path('addorder/', views.addorder, name='addorder'),
    path('clients/', views.Clients, name='clients'),
    path('clients/<str:Client_Name>/', views.Client_detail, name='Client_detail'),
    path('clients/<str:Client_Name>/<int:Order_Id>', views.Client_order_detail, name='client_order_detail'),
    path('orders', views.orders, name='orders'),
    path('clients/<str:Client_Name>/<int:var>/Client_new/', views.Client_new, name='Client_new'),
    path('about', views.about, name='about'),
]
