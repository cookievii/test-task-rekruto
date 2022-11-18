# Rekruto!

----------

### Стэк технологий:

* Python == 3.10
* django == 4.1.3
* gunicorn == 20.1.0
* psycopg2-binary == 2.9.5
* python-dotenv == 0.21.0

### Основное задание

* Создать веб-сервис, который будет выводить "Rekruto! Давай дружить!". 
URL с GET запросом, который будет выводиться уже на странице: урл должен быть таким: 
"url_name/?name=Rekruto&message=Давай дружить!"
 и выводиться на странице Hello {name}! {message}!

## Установка и запуск

```bash
# - Скачиваем проект.
git clone git@github.com:cookievii/test-task-rekruto.git

# - Переходим в директорию проекта 
cd test-task-rekruto

# - Запускаем docker-compose
docker-compose up
````

***

## Энтпоинты для работы:

```GET``` ```http://127.0.0.1/``` - Встречает текст: "Rekruto! Давай дружить!"

```GET``` ```http://127.0.0.1/?name={name}&message={massage}"``` - Выводит текст: Hello {name}! {message}!

----------

### MIT License:

Copyright (c) 2022 [cookievii](https://github.com/cookievii)

