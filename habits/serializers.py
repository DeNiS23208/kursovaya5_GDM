from rest_framework import serializers
from .models import Habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        read_only_fields = ("user",)

    def validate(self, data):
        # награда и связанная привычка не могут быть указаны одновременно
        if data.get("reward") and data.get("related_habit"):
            raise serializers.ValidationError(
                "Нельзя указывать одновременно награду и связанную привычку."
            )

        # продолжительность ≤ 120
        if data.get("duration") and data["duration"] > 120:
            raise serializers.ValidationError(
                "Время выполнения не может превышать 120 секунд."
            )

        # связанная привычка должна быть приятной
        related = data.get("related_habit")
        if related and not related.is_pleasant:
            raise serializers.ValidationError(
                "Можно привязывать только приятные привычки."
            )

        # приятная привычка не может иметь награду или связанную привычку
        if data.get("is_pleasant") is True and (
            data.get("reward") or data.get("related_habit")
        ):
            raise serializers.ValidationError(
                "Приятная привычка не может иметь награду или связанную привычку."
            )

        # периодичность не более 7
        if data.get("periodicity") and data["periodicity"] > 7:
            raise serializers.ValidationError(
                "Периодичность не может быть больше 7 дней."
            )

        return data
