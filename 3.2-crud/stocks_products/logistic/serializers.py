from rest_framework import serializers

from logistic.models import Product, StockProduct, Stock


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description',]


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['stock', 'product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = [id, 'address', 'products', 'positions']

    # настроим сериализатор для склада

    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # создаем склад по его параметрам
        stock = super().create(validated_data)

        # заполняем таблицу StockProduct с помощью списка positions
        for position in positions:
            StockProduct.objects.create(
                stock=stock,
                product=positions['product'],
                quantity=positions['quantity'],
                price=position['price'],
            )

        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)

        # обновляем таблицу StockProduct с помощью списка positions
        for position in positions:
            StockProduct.objects.update_or_create(
                stock=stock,
                product=position.get('product'),
                defaults={
                    'quantity': position.get('quantity'),
                    'price': position.get('price')
                }
            )

        return stock
