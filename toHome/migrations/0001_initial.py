# Generated by Django 4.2.2 on 2023-07-07 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("toLogin", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="categoria",
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
                ("nombre", models.CharField(max_length=200)),
                ("descripcion", models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name="cupon",
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
                ("codigo", models.CharField(max_length=200)),
                ("descripcion", models.CharField(max_length=2000)),
                ("descuento", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name="estado_pedido",
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
                ("descripcion", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="producto",
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
                ("nombre", models.CharField(max_length=200)),
                ("descripcion", models.CharField(max_length=200)),
                ("igv", models.BooleanField(default=True)),
                ("imagen", models.FileField(upload_to="")),
                ("precio", models.DecimalField(decimal_places=2, max_digits=10)),
                ("descuento", models.DecimalField(decimal_places=2, max_digits=10)),
                ("imagen1", models.FileField(upload_to="")),
                (
                    "categoria",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="toHome.categoria",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="pedido",
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
                ("fecha", models.DateTimeField(auto_now_add=True)),
                ("subtotal", models.DecimalField(decimal_places=2, max_digits=10)),
                ("igv", models.DecimalField(decimal_places=2, max_digits=10)),
                ("total", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "cupon",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="toHome.cupon",
                    ),
                ),
                (
                    "estado",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="toHome.estado_pedido",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="toLogin.customuser",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="detalle_pedido",
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
                ("cantidad", models.IntegerField()),
                ("subtotal", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "pedido",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="toHome.pedido"
                    ),
                ),
                (
                    "producto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="toHome.producto",
                    ),
                ),
            ],
        ),
    ]