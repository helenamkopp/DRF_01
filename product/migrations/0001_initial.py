# Generated by Django 3.2.4 on 2021-06-23 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(verbose_name='price')),
                ('gtin', models.CharField(default='', max_length=70, verbose_name='gtin')),
            ],
        ),
    ]
