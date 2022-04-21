
from rest_framework import serializers
from .models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        field = (
            'id',
            'title',
            'model',
            'color',
            'year',
            'price'
        )