from rest_framework import serializers

from products.models import Discount, Products, Categories


# class ProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=64)
#     price = serializers.IntegerField()
#     # discount = serializers.PrimaryKeyRelatedField(queryset=Discount.objects.all(), many=True)
#     description = serializers.CharField(max_length=128)
#
#     def create(self, validated_data):
#         return Products.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get("name")
#         # instance.category = validated_data.get("category")
#         instance.price = validated_data.get("price")
#         instance.description = validated_data.get("description")
