# Generated by Django 3.2.4 on 2021-06-23 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_gtin'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(default='', max_length=70, verbose_name='brand'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='', max_length=70, verbose_name='category'),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(default='', max_length=70, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default='', max_length=70, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0, verbose_name='price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='gtin',
            field=models.CharField(default='', max_length=70, verbose_name='gtin'),
        ),
    ]
