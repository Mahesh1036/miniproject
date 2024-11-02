from rest_framework import serializers
from .models import FitnessCalculator


class FitnessCalculatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = FitnessCalculator
        fields = ['id', 'age', 'gender', 'height', 'weight', 'activity_level']

