# Тестовое задание отдел бэкенд Сарафан

Реализовать Django проект магазина продуктов.

## Установка

1. Клонируйте репозиторий.
2. Установите зависимости.
```bash
   pip install -r requirements.txt
```
3. Перейдите в корневую папку проекта.
```bash
   cd shop
```
4. Создайте и примените миграции.
```bash
   python manage.py makemigrations
   python manage.py migrate
```
5. Создайте суперпользователя для доступа к админке.
```bash
   python manage.py createsuperuser
```
6. Запустите сервер разработки.
```bash
   python manage.py runserver
```

## Доступные эндпоинты
Админка проекета:
```
GET: admin/
```
Регистрация пользователя и получение токена:
```
POST: api/users/register/
POST: api/users/token/
```
Список категорий и продуктов (доступны всем пользователям):
```
GET: api/categories/
GET: api/products/
```
Корзина продуктов (только для авторизированных пользователей):
```
GET: api/cart/
DELETE: api/cart/clear/
POST, PUT, DELETE: api/cart/items/
```
