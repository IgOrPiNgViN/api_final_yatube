# Проект «API для Yatube»
## Кратко о проекте
Данный проект представляет собой API к Yatube. Позволяет делать запросы к эндпоинтам и получать сериализованные ответы.

## Как запустить проект
### Клонировать репозиторий и перейти в него в командной строке:

```git clone https://github.com/DmitHint/api_final_yatube.git```

```cd api_final_yatube```
### Cоздать и активировать виртуальное окружение:

```python -m venv venv```
```source venv/bin/activate```
### Установить зависимости из файла requirements.txt:

```python -m pip install --upgrade pip```
```pip install -r requirements.txt```
### Выполнить миграции:

```
python manage.py makemigraions
python manage.py migrate
```
### Запустить проект:

```python manage.py runserver```

## Работа с API
Документация для API Yatube: http://127.0.0.1:8000/redoc/.

### Примеры
---
***получение публикации по id***

`GET /api/v1/posts/{id}/`

Response

>Статус 200 - удачное выполнение запроса
```json
{
 "id": 0,   
 "author": "string",  
 "text": "string",  
 "pub_date": "2023-03-21T11:25:10Z",  
 "image": "string", 
 "group": 0 
}
```
>Статус 404 - попытка запроса несуществующей публикации
```json
{
  "detail": "Страница не найдена."
}
```
---
***создание публикации***

`POST /api/v1/posts/`

Request

```json
{
 "text": "string",
 "image": "string",
 "group": 0
}
```
Response

>Статус 200 - удачное выполнение запроса

```json
{
 "id": 0,
 "author": "string",
 "text": "string",
 "pub_date": "2023-03-21T11:25:10Z",
 "image": "string",
 "group": 0
}
```

>Статус 400 - отсутствует обязательное поле в теле запроса

```json
{
 "text": [
    "Обязательное поле."
 ]
}
```

>Статус 401 - запрос от имени анонимного пользователя

```json
{
 "detail": "Учетные данные не были предоставлены."
}
```
