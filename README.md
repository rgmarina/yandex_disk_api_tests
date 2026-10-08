# Yandex Disk API Tests

Проект автоматизированного тестирования REST API Яндекс.Диска, разработанный в рамках тестового задания.

Автотесты проверяют работу HTTP-методов **GET, POST, PUT и DELETE**, включая позитивные и негативные сценарии.

## Тестируемый сервис

**Yandex Disk REST API**

Базовый URL:

```text
https://cloud-api.yandex.net/v1/disk
```

## Покрытие тестами

В проекте реализовано **8 автоматизированных тестов**.

| HTTP-метод | Тест | Ожидаемый результат |
|---|---|---|
| GET | Получение информации о Диске | 200 OK |
| GET | Получение информации о существующей папке | 200 OK |
| GET | Получение несуществующей папки | 404 Not Found |
| POST | Копирование папки | 201 Created / 202 Accepted |
| PUT | Создание новой папки | 201 Created |
| PUT | Повторное создание существующей папки | 409 Conflict |
| DELETE | Удаление существующей папки | 204 No Content / 202 Accepted |
| DELETE | Удаление несуществующей папки | 404 Not Found |

Тесты проверяют не только HTTP-статусы, но и содержимое JSON-ответов, типы ресурсов и результат выполнения операций.

## Установка и запуск

### 1. Клонирование репозитория

```bash
git clone https://github.com/USERNAME/yandex-disk-api-tests.git
cd yandex-disk-api-tests
```

Замените `USERNAME` на имя владельца GitHub-репозитория.

### 2. Создание виртуального окружения

Для macOS:

```bash
python3 -m venv .venv
```

Активация:

```bash
source .venv/bin/activate
```

### 3. Установка зависимостей

```bash
python -m pip install -r requirements.txt
```

### 4. Настройка OAuth-токена

Для выполнения интеграционных тестов необходим действующий OAuth-токен **отдельной тестовой учётной записи Яндекса** с необходимыми правами доступа к Яндекс.Диску.

Создайте файл `.env` на основе шаблона:

```bash
cp .env.example .env
```

Укажите токен:

```dotenv
YANDEX_DISK_TOKEN=your_test_oauth_token
```

Необходимые разрешения OAuth:

- `cloud_api:disk.info` — получение информации о Диске
- `cloud_api:disk.read` — чтение ресурсов
- `cloud_api:disk.write` — управление ресурсами

Файл `.env` добавлен в `.gitignore` и не публикуется на GitHub.

### 5. Проверка обнаружения тестов

```bash
python -m pytest --collect-only -q
```

### 6. Запуск всех тестов

```bash
python -m pytest -v
```

### 7. Запуск тестов отдельного HTTP-метода

GET:

```bash
python -m pytest tests/test_get.py -v
```

POST:

```bash
python -m pytest tests/test_post.py -v
```

PUT:

```bash
python -m pytest tests/test_put.py -v
```

DELETE:

```bash
python -m pytest tests/test_delete.py -v
```

### 8. Запуск одного теста

```bash
python -m pytest tests/test_get.py::test_get_disk_info -v
```