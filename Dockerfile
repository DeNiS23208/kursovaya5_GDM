FROM python:3.10-slim

WORKDIR /app

COPY . /app


RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "kursovaya5_GDM.wsgi:application", "--bind", "0.0.0.0:8000"]