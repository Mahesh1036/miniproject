from django.db import models

# Create your models here.



class FitnessCalculator(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female')
    ]

    ACTIVITY_LEVEL_CHOICES = [
        ('sedentary', 'Sedentary: little or no exercise'),
        ('light', 'Light: exercise 1-3 times/week'),
        ('moderate', 'Moderate: exercise 4-5 times/week'),
        ('active', 'Active: daily exercise or intense exercise 3-4 times/week'),
        ('very_active', 'Very Active: intense exercise 6-7 times/week'),
    ]

    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    height = models.FloatField(help_text="Height in cm")
    weight = models.FloatField(help_text="Weight in kg")
    activity_level = models.CharField(max_length=20, choices=ACTIVITY_LEVEL_CHOICES)

    def __str__(self):
        return f'{self.age} - {self.gender} - {self.activity_level}'
