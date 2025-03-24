Краткий конспект изученных технологий

1. Docker

Используется для контейнеризации, обеспечивая изолированную среду для приложений.

Основные команды:

docker build -t my_image .
docker run -d --name my_container my_image
docker-compose up -d

2. Docker Compose

Позволяет управлять многоконтейнерными приложениями с помощью docker-compose.yml.

Преимущества:

Автоматизирует запуск зависимых сервисов (PgAdmin, PostgreSQL и MinIO).

Позволяет передавать переменные окружения через .env файл.

3. PostgreSQL

Популярная реляционная база данных с открытым исходным кодом.

Используемые библиотеки:

psycopg2 — взаимодействие с базой данных.

COPY FROM — массовый импорт данных из CSV.

4. MinIO

Объектное хранилище, совместимое с Amazon S3.

Используемые библиотеки:

boto3 — загрузка и скачивание файлов из MinIO.

5. PgAdmin

UI-инструмент для работы с PostgreSQL.

6. Python-скрипты

boto3 — работа с MinIO.

psycopg2 — взаимодействие с PostgreSQL.

dotenv — управление переменными окружения.

7. Управление переменными окружения

Использование .env для хранения конфиденциальных данных и избежания хардкодинга.

8. Git и файлы исключений

.gitignore — предотвращает попадание в репозиторий ненужных файлов (venv, логи).

.dockerignore — оптимизирует сборку Docker-образов.

Этапы выполнения задания

1. Настройка файлов окружения

Создаем файл .env в корневой директории проекта и добавляем переменные:

# PostgreSQL
DB_HOST=postgres
DB_PORT=5432
DB_USER=your_db_user
DB_PASS=your_db_password
DB_NAME=your_db_name

# MinIO
S3_ENDPOINT_URL=http://localhost:9000
S3_ACCESS_KEY=your_access_key
S3_SECRET_KEY=your_secret_key
S3_BUCKET_NAME=your_bucket_name

# pgAdmin (если требуется)
PGADMIN_DEFAULT_EMAIL=your_email@example.com
PGADMIN_DEFAULT_PASSWORD=your_pgadmin_password

2. Создание docker-compose.yml

Определяем конфигурацию сервисов, используя .env файл:

version: '3.8'
services:
  postgres:
    image: postgres:16
    restart: always
    env_file:
      - .env
    ports:
      - "5433:5432"
    volumes:
      - ./pgdata:/var/lib/postgresql/data

Запуск сервисов:

docker-compose up -d

Проверка работающих контейнеров:

docker ps

3. Изменение конфигурации pg_hba.conf для удобного подключения

Для подключения к PostgreSQL в контейнере обновляем pg_hba.conf:

docker exec -it postgres_db bash
vi /var/lib/postgresql/data/pg_hba.conf

Изменяем:

host    all             all             0.0.0.0/0               trust

Перезапускаем контейнер:

docker restart postgres_db

4. Создание скриптов для автоматизации
Скрипт для загрузки данных в Postgres load_postgres.py
Скрипт для загрузки данных в Minio upload_s3.py
