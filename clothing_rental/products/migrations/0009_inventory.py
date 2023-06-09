# Generated by Django 4.2.1 on 2023-06-01 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "products",
            "0008_rename_clothing_item_id_clothingconfiguration_clothing_item_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Inventory",
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
                ("detail", models.CharField(max_length=200)),
                ("code", models.CharField(max_length=100)),
                ("price", models.DecimalField(decimal_places=2, max_digits=60)),
                (
                    "clothes_item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.clothingitem",
                    ),
                ),
            ],
        ),
    ]
