<h2 align="center">PySoNet by Django</h2>

Социальная сеть на Django Rest Framework.

**Ссылки**:
- [Сайт](https://djangochannel.com)
- [YouTube](https://www.youtube.com/playlist?list=PLF-NY6ldwAWqSxUpnTBObEP21cFQxNJ7C)
- [Telegram](https://t.me/trueDjangoChannel)
- [Группа в VK](https://vk.com/djangochannel)
- [Поддержать проект](https://donatepay.ru/don/186076)
### Инструменты разработки

**Стек:**
- Python >= 3.8
- Django Rest Framework
- Postgres

## Старт

#### 1) Создать образ

    docker-compose build

##### 2) Запустить контейнер

    docker-compose up
    
##### 3) Перейти по адресу

    http://127.0.0.1:8000/api/v1/swagger/

## Разработка с Docker

##### 1) Сделать форк репозитория

##### 2) Клонировать репозиторий

    git clone ссылка_сгенерированная_в_вашем_репозитории

##### 3) В корне проекта создать .env.dev

    DEBUG=1
    SECRET_KEY=fdsadqw3f32wg<43g3hv$%#@%F$F$$F$F
    DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
    
    # Data Base
    POSTGRES_DB=pysonet
    POSTGRES_ENGINE=django.db.backends.postgresql
    POSTGRES_DATABASE=pysonet
    POSTGRES_USER=pysonet_user
    POSTGRES_PASSWORD=pysonet_pass
    POSTGRES_HOST=pysonet-db
    POSTGRES_PORT=5432
    DATABASE=postgres

    # Email
    DEFAULT_FROM_EMAIL=your@your.com
    EMAIL_USE_TLS=True
    EMAIL_HOST=your_smtp
    EMAIL_HOST_USER=your@your.com
    EMAIL_HOST_PASSWORD=pass
    EMAIL_PORT=587
    
##### 4) Создать образ

    docker-compose build

##### 5) Запустить контейнер

    docker-compose up
    
##### 6) Создать суперюзера

    docker exec -it pysonet_pysonet_back_1 python manage.py createsuperuser
                                                        
##### 7) Если нужно очистить БД

    docker-compose down -v
 
## License

[BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause)

Copyright (c) 2020-present, DJWOMS - Omelchenko Michael




