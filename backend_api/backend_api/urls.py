from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from backend_api.api import views

router = routers.DefaultRouter()

urlpatterns = [
    path('', views.api_root),
    path('orders/', views.OrderList.as_view(), name='order-list'),
    path('orders/<int:pk>/', views.OrderDetail.as_view()),
    path('pizzas/', views.PizzaList.as_view(), name='pizza-list'),
    path('pizzas/<int:pk>/', views.PizzaDetail.as_view()),
]