# Generated by Django 3.1.2 on 2020-10-28 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_product_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='balance',
            field=models.FloatField(default=0),
        ),
    ]
