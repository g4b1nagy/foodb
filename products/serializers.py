from rest_framework import serializers

from .models import Product, Batch


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'created_on', 'updated_on', 'name', 'description']


class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = ['id', 'created_on', 'updated_on', 'product', 'amount', 'expires_on']
