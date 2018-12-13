from rest_framework import serializers
from .models import Order, Pizza


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('pizza',
                  'customer_name', 'customer_address',
                  'description', 'size')


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = ('name',)
