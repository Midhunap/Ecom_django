# Generated by Django 3.1 on 2021-12-22 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_auto_20211222_0626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cart_id',
            field=models.CharField(max_length=250, null=True),
        ),
    ]