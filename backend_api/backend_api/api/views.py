# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Order, Pizza
from .serializers import OrderSerializer, PizzaSerializer


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class PizzaList(generics.ListCreateAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


class PizzaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'orders': reverse('order-list', request=request, format=format),
        'pizzas': reverse('pizza-list', request=request, format=format),
    })
