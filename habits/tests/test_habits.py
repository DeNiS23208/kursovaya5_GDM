import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from habits.models import Habit

User = get_user_model()


@pytest.mark.django_db
def test_create_habit():
    client = APIClient()

    user = User.objects.create_user(
        email="test@example.com", username="test", password="pass"
    )

    assert user.username == "test"

    response = client.post(
        "/api/users/login/", data={"email": "test@example.com", "password": "pass"}
    )
    token = response.data["access"]
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    data = {
        "place": "Дом",
        "time": "07:00",
        "action": "Пить воду",
        "is_pleasant": False,
        "periodicity": 1,
        "duration": 60,
        "is_public": True,
    }
    response = client.post("/api/habits/", data)
    assert response.status_code == 201
    assert Habit.objects.count() == 1
    assert Habit.objects.first().action == "Пить воду"
