# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import force_authenticate
from .models import Order, Pizza

class APITests(APITestCase):
    def test_create_pizza(self):
        url = reverse('pizza-list')
        data = dict(name="Pepperoni")
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], "Pepperoni")
        self.assertEqual(Pizza.objects.all().first().name, "Pepperoni")

    def test_create_order(self):
        """
        Ensure we can create a new order object.
        """
        url = reverse('order-list')
        Pizza.objects.create(name="Mozarela")
        data = dict(customer_name='Dio', customer_address='Test, 50', pizza=1, description="Chocolate border")
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.get().customer_name, 'Dio')
