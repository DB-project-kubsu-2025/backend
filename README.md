# backend
Репозиторий, в котором хранится кодовая база серверной части (в том числе ML) веб-приложения для проекта по базам данных

## Системные требования
1. Docker
2. Python

## Документация по развертыванию

1. Запустить docker desktop (он должен быть запущен)
2. В терминале в корне проекта запустить команду:
    ```bash
    docker compose build
    ```
3. В том же терминале запустить команду:
    ```bash
    docker compose up
    ```

## Настройка интерпретатора в PyCharm Professional
1. Settings -> Project -> Python Interpreter -> Add Interpreter -> On docker compose
2. Configuration files: ./docker-compose.yaml, service: app
3. Все последующие настройки не меняем
