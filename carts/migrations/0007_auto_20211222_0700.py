# Generated by Django 3.1 on 2021-12-22 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0006_auto_20211222_0639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]