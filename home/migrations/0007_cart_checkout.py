# Generated by Django 4.1.7 on 2023-03-31 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0006_cart"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="checkout",
            field=models.BooleanField(default=False),
        ),
    ]
