from rest_framework import serializers

from core.models import User
from customers.models import Costumers


class UserSerializer(serializers.ModelSerializer):
    model = User
    fields = "__all__"


class CostumerSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    user = UserSerializer(many=True, read_only=True)
