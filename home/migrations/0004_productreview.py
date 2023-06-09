# Generated by Django 4.1.7 on 2023-03-23 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_brand_slug"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductReview",
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
                ("name", models.CharField(max_length=300)),
                ("email", models.EmailField(max_length=300)),
                ("review", models.TextField(blank=True)),
                ("star", models.IntegerField()),
                ("slug", models.TextField()),
                ("date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
