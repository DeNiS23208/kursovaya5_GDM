import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
def test_user_registration_and_login():
    client = APIClient()

    # Регистрация
    register_data = {
        "email": "user@example.com",
        "username": "user",
        "password": "strongpass123",
    }
    response = client.post("/api/users/register/", register_data)
    assert response.status_code == 201

    # Авторизация
    login_data = {"email": "user@example.com", "password": "strongpass123"}
    response = client.post("/api/users/login/", login_data)
    assert response.status_code == 200
    assert "access" in response.data
