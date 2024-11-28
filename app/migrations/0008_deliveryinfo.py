# Generated by Django 5.0.4 on 2024-05-04 06:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0007_category_alter_product_details_alter_product_image_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="DeliveryInfo",
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
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=15)),
                ("name", models.CharField(max_length=100)),
                ("address", models.TextField()),
                ("country", models.CharField(max_length=100)),
                ("state", models.CharField(max_length=100)),
                ("city", models.CharField(max_length=100)),
                ("zipcode", models.CharField(max_length=10)),
            ],
        ),
    ]