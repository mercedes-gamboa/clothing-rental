# Generated by Django 4.2.1 on 2023-06-01 09:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("products", "0009_inventory"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
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
                ("created_date", models.DateField(auto_now_add=True)),
                ("date_to_be_returned", models.DateField()),
                (
                    "confirmed_returned_date",
                    models.DateField(default=models.DateField()),
                ),
                ("total_price", models.DecimalField(decimal_places=2, max_digits=60)),
                ("code", models.CharField(max_length=100)),
                (
                    "clothing_item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.clothingitem",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrderStatus",
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
                ("status", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="OrderLine",
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
                (
                    "inventory",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.inventory",
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="orders.order"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="order",
            name="status",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="orders.orderstatus"
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="user_order_set",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
