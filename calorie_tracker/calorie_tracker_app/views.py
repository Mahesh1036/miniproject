from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from .models import FitnessCalculator
from .serializers import FitnessCalculatorSerializer


class FitnessCalculatorViewSet(viewsets.ModelViewSet):
    queryset = FitnessCalculator.objects.all()
    serializer_class = FitnessCalculatorSerializer

    def create(self, request, *args, **kwargs):
        age = int(request.data['age'])
        gender = request.data['gender']
        height = float(request.data['height'])
        weight = float(request.data['weight'])
        activity_level = request.data['activity_level']

        if gender == 'male':
            bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
        else:
            bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

        activity_multiplier = {
            'sedentary': 1.2,
            'light': 1.375,
            'moderate': 1.55,
            'active': 1.725,
            'very_active': 1.9
        }

        maintenance_calories = bmr*activity_multiplier[activity_level]

        results = {
            "maintain_weight": int(maintenance_calories),
            "mild_weight_loss": int(maintenance_calories * 0.9),  # 10% deficit
            "weight_loss": int(maintenance_calories * 0.8),  # 20% deficit
            "extreme_weight_loss": int(maintenance_calories * 0.6)  # 40% deficit
        }

        return Response(results)