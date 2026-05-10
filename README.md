# СКЛАД v1.0 — Система складского учёта

Веб-приложение для учёта товаров на складе с привязкой к организациям.

## Возможности

- Учёт товаров с категориями
- Контроль минимальных остатков
- Статистика: общее количество, низкие остатки, стоимость остатков
- Фильтрация по категориям
- Админ-панель Django

## Требования

- Python 3.10+
- Django 4.2+

## Установка

```bash
# Клонирование
git clone https://github.com/YOUR_USERNAME/sklad.git
cd sklad

# Создание виртуального окружения
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate  # Windows

# Установка зависимостей
pip install django

# Применение миграций
cd sklad
python manage.py migrate

# Создание суперпользователя
python manage.py createsuperuser

# Запуск сервера
python manage.py runserver
```

## Использование

1. Откройте `http://127.0.0.1:8000/admin` и войдите
2. Создайте организации в админке
3. Перейдите на `http://127.0.0.1:8000/`
4. Выберите организацию и работайте с товарами

## Структура проекта

```
diplom/
├── sklad/                 # Django-проект
│   ├── inventory/         # Приложение учёта
│   │   ├── models.py      # Модели данных
│   │   ├── views.py       # Логика
│   │   ├── forms.py       # Формы
│   │   └── urls.py        # Маршруты
│   ├── templates/         # HTML-шаблоны
│   ├── static/            # CSS
│   └── settings.py        # Настройки
├── presentation.md        # Презентация
└── README.md              # Этот файл
```

## Технологии

- Python + Django 4
- SQLite (встроенная БД)
- Bootstrap 5
- HTML/CSS/JS

## Лицензия

MIT