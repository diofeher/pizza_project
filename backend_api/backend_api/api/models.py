# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Pizza(models.Model):
    name = models.CharField(max_length=32)


PIZZA_SIZES = (
    (30, '30cm'),
    (50, '50cm')
)
class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    customer_name = models.CharField(max_length=32)
    customer_address = models.CharField(max_length=100)
    pizza = models.ForeignKey(Pizza, on_delete=models.DO_NOTHING)
    description = models.TextField(blank=True)
    size = models.IntegerField(choices=PIZZA_SIZES, default=30)

    class Meta:
        ordering = ('created',)