# Generated by Django 4.2.1 on 2023-05-30 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0007_clothingitem_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="clothingconfiguration",
            old_name="clothing_item_id",
            new_name="clothing_item",
        ),
        migrations.RenameField(
            model_name="clothingconfiguration",
            old_name="variation_option_id",
            new_name="variation_option",
        ),
    ]
