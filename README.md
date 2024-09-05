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
      {
        "username": "name",
        "password": "12345"
      }
   POST: api/users/token/
      {
        "username": "name",
        "password": "12345"
      }
```
Список категорий и продуктов (доступны всем пользователям):
```
   GET: api/categories/
   GET: api/products/
```
Корзина продуктов (только для авторизированных пользователей):
```
   GET: api/cart/ - список продуктов в корзине
   DELETE: api/cart/clear/ - полная очистка корзины
   POST, PUT, DELETE: api/cart/items/ - добавление, изменение количества и удаление продукта
```
