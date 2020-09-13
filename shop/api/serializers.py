from rest_framework import serializers
from shop.models import CoffeeMachine,CoffePod


class machineSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeeMachine
        fields = ('SKU',)


class podSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffePod
        fields = ('SKU',)