import pytest
from habits.models import Habit
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()


@pytest.mark.django_db
def test_habit_validator_fails_on_duration_over_120():
    user = User.objects.create_user(email="v@example.com", username="v", password="123")
    habit = Habit(
        user=user,
        place="Дом",
        time="07:00",
        action="Медитация",
        duration=130,
        is_pleasant=False,
        periodicity=1,
    )
    with pytest.raises(ValidationError):
        habit.clean()
