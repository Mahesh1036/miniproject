from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import FitnessCalculatorViewSet

router = DefaultRouter()
router.register(r'fitness', FitnessCalculatorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
