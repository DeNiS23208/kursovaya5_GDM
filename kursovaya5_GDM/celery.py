import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kursovaya5_GDM.settings")

app = Celery("kursovaya5_GDM")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
