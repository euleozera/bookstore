# Generated by Django 4.1.3 on 2022-11-21 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="category",
            old_name="descriqtion",
            new_name="description",
        ),
        migrations.RenameField(
            model_name="product",
            old_name="prince",
            new_name="price",
        ),
    ]
