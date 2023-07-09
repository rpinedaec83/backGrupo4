from decimal import Decimal
from rest_framework import serializers
from .models import Cupon, Estado_pedido, Pedido, Detalle_pedido


class CuponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cupon
        fields = '__all__'


class EstadoPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado_pedido
        fields = '__all__'


class DetallePedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalle_pedido
        fields = ['producto', 'cantidad', 'subtotal']


class PedidoSerializer(serializers.ModelSerializer):
    detalles = DetallePedidoSerializer(many=True)

    class Meta:
        model = Pedido
        fields = '__all__'

    def create(self, validated_data):
        detalles_data = validated_data.pop('detalles')

        # Obtener el porcentaje de descuento del cupón
        cupon = validated_data.get('cupon')
        porcentaje_descuento = cupon.descuento if cupon else 0

        pedido = Pedido.objects.create(**validated_data)

        subtotal = Decimal(0)
        for detalle_data in detalles_data:
            det = Detalle_pedido.objects.create(pedido=pedido, **detalle_data)
            subtotal += det.subtotal

         # Aplicar el descuento al total
        total = subtotal - (subtotal * porcentaje_descuento / 100)
        pedido.total = total
        pedido.save()

        return pedido
