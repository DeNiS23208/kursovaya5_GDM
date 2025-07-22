from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import HabitViewSet

router = DefaultRouter()
router.register("", HabitViewSet, basename="habit")

urlpatterns = [
    path("", include(router.urls)),
]
