# Generated by Django 4.2.2 on 2023-07-07 02:38

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("toHome", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="detalle_pedido",
            name="pedido",
        ),
        migrations.RemoveField(
            model_name="detalle_pedido",
            name="producto",
        ),
        migrations.RemoveField(
            model_name="pedido",
            name="cupon",
        ),
        migrations.RemoveField(
            model_name="pedido",
            name="estado",
        ),
        migrations.RemoveField(
            model_name="pedido",
            name="user",
        ),
        migrations.DeleteModel(
            name="cupon",
        ),
        migrations.DeleteModel(
            name="detalle_pedido",
        ),
        migrations.DeleteModel(
            name="estado_pedido",
        ),
        migrations.DeleteModel(
            name="pedido",
        ),
    ]
