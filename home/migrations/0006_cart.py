# Generated by Django 4.1.7 on 2023-03-31 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0005_alter_productreview_star"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cart",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=300)),
                ("slug", models.TextField()),
                ("quntity", models.IntegerField(default=1)),
                ("total", models.IntegerField()),
                (
                    "items",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.product"
                    ),
                ),
            ],
        ),
    ]
