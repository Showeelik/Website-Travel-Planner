# Travel Planner

**Travel Planner** — это веб-приложение для создания и управления маршрутами путешествий. Пользователи могут создавать маршруты, оставлять отзывы и получать уведомления.

> **Важно:** Проект находится в стадии **альфа-разработки** и не является конечным продуктом. Возможны ошибки, недоработки и изменения функционала. Используйте на свой страх и риск.

---

## Содержание

1. [Описание проекта](#описание-проекта)
2. [Требования](#требования)
3. [Установка и запуск](#установка-и-запуск)
4. [Создатель](#создатель)
5. [Лицензия](#лицензия)

---

## Описание проекта

Travel Planner позволяет пользователям:
- Создавать и редактировать маршруты.
- Оставлять отзывы и рейтинги для маршрутов.
- Получать уведомления о новых отзывах.
- Управлять своими данными через удобный интерфейс.

Проект разрабатывается с использованием следующих технологий:
- **Backend:** Django, Django REST Framework
- **Frontend:** HTML, CSS (Bootstrap), JavaScript
- **Брокер задач:** Celery + Redis
- **База данных:** PostgreSQL (или SQLite для разработки)

---

## Требования

Для запуска проекта вам понадобятся:
- Python 3.9+
- Poetry (для управления зависимостями)
- Redis (для Celery)
- PostgreSQL (опционально, можно использовать SQLite для локальной разработки)

---

## Установка и запуск

### 1. Клонируйте репозиторий
```bash
git clone https://github.com/Showeelik/Website-Travel-Planner.git
cd Website-Travel-Planner
```

### 2. Установите зависимости
Используйте Poetry для установки зависимостей:
```bash
poetry install
```

### 3. Настройте переменные окружения
Создайте файл `.env` в корне проекта и добавьте следующие переменные:
```env
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3  # или postgres://user:password@localhost:5432/travel_planner
REDIS_HOST=localhost
REDIS_PORT=6379
```

### 4. Примените миграции
```bash
python manage.py migrate
```

### 5. Запустите Redis
Убедитесь, что Redis запущен:
```bash
redis-server
```

### 6. Запустите Celery
Запустите Celery worker:
```bash
celery -A travel_planner worker --loglevel=info
```

### 7. Запустите сервер разработки
```bash
python manage.py runserver
```

Теперь приложение доступно по адресу: [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## Создатель

Проект создан **[@Showeelik](https://github.com/Showeelik)**.  
Если у вас есть вопросы или предложения, свяжитесь со мной:
- Email: zeezxex2006@mail.ru
- GitHub: **[@Showeelik](https://github.com/Showeelik)**

---

## Лицензия

Этот проект распространяется под лицензией **MIT License**. Это означает, что вы можете свободно использовать, изменять и распространять код, но автор не несет ответственности за возможные последствия его использования.

Полный текст лицензии можно найти в файле [LICENSE](LICENSE).

---

### Примечания

- Если вы хотите внести вклад в проект, создайте issue или pull request.
- Для production-среды рекомендуется использовать PostgreSQL вместо SQLite и настроить HTTPS.