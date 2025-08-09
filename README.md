# 📌 Трекер полезных привычек

Проект Django REST Framework для отслеживания и управления полезными привычками с напоминаниями. Реализована интеграция с Telegram, Celery для фоновых задач, Redis как брокер, PostgreSQL как БД, и автоматический деплой на сервер через GitHub Actions.

---

## 🚀 Возможности

- Регистрация и авторизация пользователей
- Создание личных и публичных привычек
- Уведомления через Telegram
- Автоматические напоминания с Celery и Beat
- Права доступа: только владелец может редактировать привычки
- Документация OpenAPI/Swagger
- CI/CD с тестами и автодеплоем

---

## 🛠️ Стек технологий

- Python 3.10
- Django 4+
- Django REST Framework
- PostgreSQL
- Redis
- Celery + Celery Beat
- Docker, Docker Compose
- GitHub Actions (CI/CD)
- Yandex Cloud (деплой)

---

## 🔧 Установка и запуск проекта локально (Docker)

1. **Клонируй репозиторий:**
   ```bash
   git clone https://github.com/DeNiS23208/kursovaya5_GDM.git
   cd kursovaya5_GDM
   ```

2. **Создай `.env` на основе шаблона:**
   ```env
   SECRET_KEY=укажи_свой_секретный_ключ
   DEBUG=True
   ALLOWED_HOSTS=127.0.0.1,localhost

   DATABASE_NAME=postgres
   DATABASE_USER=postgres
   DATABASE_PASSWORD=postgres
   DATABASE_HOST=db
   DATABASE_PORT=5432

   CELERY_BROKER_URL=redis://redis:6379/0
   ```

3. **Собери и запусти проект:**
   ```bash
   docker compose up --build
   ```

4. **Открой в браузере:**
   ```
   http://localhost
   ```

---

## ⚙️ Миграции и статика

Команды автоматически выполняются при запуске контейнера `backend`:
- `python manage.py migrate`
- `python manage.py collectstatic --noinput`

---

## 🧪 Тестирование

Встроены базовые тесты.

Запуск вручную:
```bash
docker compose exec backend pytest
```

---

## 🔁 CI/CD

- Настроен GitHub Actions workflow `.github/workflows/deploy.yml`
- Автоматически запускается:
  - при push в ветку `feature/kursovaya5`
  - выполняет тесты и линтинг
  - при успехе — деплой на сервер через SSH

---

## 🌐 Продакшн сервер

Приложение развернуто на сервере:

```
http://89.169.178.245
```

---

## 📦 Структура проекта

```
├── backend/                  # Приложение Django
├── config/                   # Настройки Django, wsgi.py, celery.py
├── nginx/                    # Конфигурация и Dockerfile для nginx
├── .env.template             # Шаблон конфигурации переменных
├── Dockerfile                # Docker-образ backend
├── docker-compose.yml        # Docker-оркестрация всех сервисов
├── requirements.txt          # Зависимости проекта
├── .github/workflows/        # GitHub Actions workflow
└── README.md
```

---

## 👨‍💻 Автор

**Денис**  
Курс "Профессия Python-разработчик" от SkyPro  
GitHub: [github.com/DeNiS23208](https://github.com/DeNiS23208)