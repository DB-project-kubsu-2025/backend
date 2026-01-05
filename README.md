# backend
Репозиторий, в котором хранится кодовая база серверной части (в том числе ML) веб-приложения для проекта по базам данных

## Системные требования
1. Docker
2. Python

## Документация по развертыванию

1. В проекте есть файл `db_project/db_project/.env.example`. В той же директории, где лежит `.env.example` необходимо создать файл `.env` и скопировать в него содержимое файла `.env.example` 
2. В папку `./frontend` необходимо стянуть репозиторий frontend-части проекта (https://github.com/DB-project-kubsu-2025/frontend)
    _с некоторой периодичностью frontend надо обновлять (git pull origin main или git fetch origin main:main)_
3. В .env заполнить переменные `ALLOWED_HOSTS` и `SECRET_KEY`. В первую переменную необходимо написать IP-адрес своего устройства, во вторую - любой текст
4. Запустить docker desktop (он должен быть запущен)
5. Сгенерировать ssl-сертификаты следующей командой:
   ```bash
   mkcert -cert-file ssl/crm.crt -key-file ssl/crm.key crm.com
   ```
6. На windows отредактировать (с правами админа) файл с хостами (`C:\Windows\System32\drivers\etc\hosts`), добавить туда следующие строки:
   ```bash
   <ip-адрес> crm.com
   <ip-адрес> admin.crm.com
   ```
   и не забыть сохранить
7. В том же терминале запустить команду:
    ```bash
    docker compose up
    ```
При переходе в браузере на страницу `https://crm.com/` должна отобразиться форма авторизации
При переходе в браузере на страницу `https://crm.com/admin` можно попасть в админ-панель Django. На тестовом окружении логин и пароль суперпользователя: admin 1234

## Настройка интерпретатора в PyCharm Professional
1. Settings -> Project -> Python Interpreter -> Add Interpreter -> On docker compose
2. Configuration files: ./docker-compose.yaml, service: app
3. Все последующие настройки не меняем
