from django.db import models


class Product(models.Model):
    name = models.CharField('name', max_length=255),
    description = models.CharField('description', max_length=255), 
    price = models.FloatField('price'),
    category = models.CharField('category', max_length=255),
    brand = models.CharField('brand', max_length=80, default=''), 
    gtin = models.CharField('gtin', max_length=70, default='')