import pytest
from habits.models import Habit
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()


@pytest.mark.django_db
def test_public_habits_are_visible():
    client = APIClient()
    user = User.objects.create_user(
        email="public@example.com", username="public", password="123"
    )
    Habit.objects.create(
        user=user,
        place="Парк",
        time="09:00",
        action="Бег",
        is_pleasant=False,
        periodicity=1,
        duration=50,
        is_public=True,
    )

    response = client.get("/api/habits/public/")
    assert response.status_code == 200
    assert len(response.data) == 1
