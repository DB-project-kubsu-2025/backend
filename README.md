# backend
Репозиторий, в котором хранится кодовая база серверной части (в том числе ML) веб-приложения для проекта по базам данных

## Системные требования
1. Docker
2. Python

## Документация по развертыванию

1. В проекте есть файл `db_project/db_project/.env.example`. В той же директории, где лежит `.env.example` необходимо создать файл `.env` и скопировать в него содержимое файла `.env.example` 
2. В .env заполнить переменные `ALLOWED_HOSTS` и `SECRET_KEY`. В первую переменную необходимо написать IP-адрес своего устройства, во вторую - любой текст
3. Запустить docker desktop (он должен быть запущен)
4. Сгенерировать ssl-сертификаты следующей командой:
   ```bash
   mkcert -cert-file ssl/crm.crt -key-file ssl/crm.key crm.com
   ```
5. На windows отредактировать (с правами админа) файл с хостами (`C:\Windows\System32\drivers\etc\hosts`), добавить туда следующие строки:
   ```bash
   <ip-адрес> crm.com
   <ip-адрес> admin.crm.com
   ```
   и не забыть сохранить
6. В терминале в корне проекта запустить команду:
    ```bash
    docker compose build
    ```
7. В том же терминале запустить команду:
    ```bash
    docker compose up
    ```
8. Посмотрите IP своего устройства, далее в браузере перейдите по IP и по порту 8050, URL должен быть примерно такой: `http://192.168.0.90:8050/admin`
9. В терминале выполните следующую команду:
    ```bash
    docker exec db_project-app-1 poetry run python3 manage.py migrate
    ```
10. Также в терминале запустите еще одну команду:
     ```bash
     docker exec db_project-app-1 poetry run python3 manage.py create_custom_superuser
     ```
11. Запустить frontend
При переходе в браузере на страницу `https://crm.com/` должна отобразиться форма авторизации

## Настройка интерпретатора в PyCharm Professional
1. Settings -> Project -> Python Interpreter -> Add Interpreter -> On docker compose
2. Configuration files: ./docker-compose.yaml, service: app
3. Все последующие настройки не меняем
