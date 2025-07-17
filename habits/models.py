from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError


class Habit(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="habits"
    )
    place = models.CharField(max_length=255)
    time = models.TimeField()
    action = models.CharField(max_length=255)
    is_pleasant = models.BooleanField(default=False)
    related_habit = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="related_to",
    )
    periodicity = models.PositiveSmallIntegerField(default=1)  # дни
    reward = models.CharField(max_length=255, blank=True, null=True)
    duration = models.PositiveSmallIntegerField(help_text="в секундах")
    is_public = models.BooleanField(default=False)

    def clean(self):
        # нельзя указать и вознаграждение, и связанную привычку
        if self.reward and self.related_habit:
            raise ValidationError(
                "Нельзя одновременно указывать и награду, и связанную привычку."
            )

        # время на выполнение ≤ 120 секунд
        if self.duration > 120:
            raise ValidationError("Время выполнения не может превышать 120 секунд.")

        # связанная привычка должна быть приятной
        if self.related_habit and not self.related_habit.is_pleasant:
            raise ValidationError("Можно привязывать только приятные привычки.")

        # приятная привычка не может иметь вознаграждение или связанную
        if self.is_pleasant and (self.reward or self.related_habit):
            raise ValidationError(
                "Приятная привычка не может иметь награду или связанную привычку."
            )

        # периодичность не должна превышать 7 дней
        if self.periodicity > 7:
            raise ValidationError("Периодичность не может превышать 7 дней.")

    def str(self):
        return f"{self.action} — {self.user.email}"
