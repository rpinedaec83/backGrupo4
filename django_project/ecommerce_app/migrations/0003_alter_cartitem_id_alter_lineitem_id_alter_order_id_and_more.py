# Generated by Django 4.2.2 on 2023-07-08 04:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ecommerce_app", "0002_auto_20181206_1406"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cartitem",
            name="id",
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="lineitem",
            name="id",
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="order",
            name="id",
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="product",
            name="id",
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
