from django.db import models


class Product(models.Model):
    name = models.CharField('name', max_length=70, default='')
    description = models.CharField('description', max_length=70, default='') 
    price = models.FloatField('price', default=0)
    category = models.CharField('category', max_length=70, default='')
    brand = models.CharField('brand', max_length=70, default='')
    gtin = models.CharField('gtin', max_length=70, default='')