# api_yamdb
## Описание
Backend приложения YamDB. 
Проект объединяет в себе функционал работы api сервисов проекта для публикации произведений,
отзывов и комментариев к ним. 
View- функции реализованы с помощью вьюсетов, аутентификация пользователей через JWT-токены.
Проект собран в контейнеры с помощью функционала Docker.

## Установка
```
git clone https://github.com/Markello93/yamdb_final.git
```
```
cd yamdb_final/infra
```

#### Создайте файл .env в директории infra/ и добавьте переменные окружения:
```
SECRET_KEY = 'Ваш секретный ключ django'
EMAIL_HOST_USER = ваш email
EMAIL_HOST_PASSWORD = пароль для доступа к email
EMAIL_HOST = хост почтового клиента
EMAIL_PORT = порт для email хоста
DB_ENGINE = engine дб
DB_NAME = имя Вашей дб
POSTGRES_USER = имя юзера дб
POSTGRES_PASSWORD = ваш пароль для пользования 
DB_HOST = хост для базы данных
DB_PORT = порт для базы данных
```
#### Запустите сборку контейнеров docker командой:
```
docker compose up
```

#### Выполните миграции:
```
docker-compose exec web python manage.py migrate
```
#### Скопируйте файлы статики в контейнер:
```
docker-compose exec web python manage.py collectstatic --no-input
```
#### Выполните импорт данных в базу данных (при необходимости):
```
docker-compose exec web python manage.py load_data_from_csv
```

## Примеры
Доступ к документации API представлен по ссылке:
[http://158.160.13.46/redoc/](http://158.160.13.46/redoc/)

![yamdb_workflow](https://github.com/Markello93/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
