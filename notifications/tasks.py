from celery import shared_task
from habits.models import Habit
from django.utils import timezone
import requests
import os

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


@shared_task
def send_habit_reminders():
    now = timezone.localtime()
    current_time = now.time()

    habits = Habit.objects.filter(
        timehour=current_time.hour, timeminute=current_time.minute
    )
    for habit in habits:
        user = habit.user
        if not user.telegram_chat_id:
            continue

        text = f"Напоминание: {habit.action} в {habit.place} — пора выполнять!"
        url = (
            f"[https://api.telegram.org/bot{BOT_TOKEN}"
            f"/sendMessage](https://api.telegram.org/bot{BOT_TOKEN}/sendMessage)"
        )
        data = {"chat_id": user.telegram_chat_id, "text": text}
        requests.post(url, data=data)
