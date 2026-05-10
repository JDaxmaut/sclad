FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir django

COPY . .

RUN python manage.py migrate --noinput

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]