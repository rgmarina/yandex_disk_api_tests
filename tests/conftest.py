
import os
import uuid

import pytest
from dotenv import load_dotenv

from api.client import YandexDiskClient


load_dotenv()


@pytest.fixture(scope="session")
def client():
    token = os.getenv("YANDEX_DISK_TOKEN")

    if not token or token == "your_test_oauth_token_here":
        pytest.fail(
            "Не найден тестовый OAuth-токен. "
            "Добавьте YANDEX_DISK_TOKEN в файл .env",
            pytrace=False,
        )

    disk_client = YandexDiskClient(token)

    yield disk_client

    disk_client.close()


@pytest.fixture
def test_folder(client):
    folder_name = f"api_tests_{uuid.uuid4().hex}"
    folder_path = f"disk:/{folder_name}"

    response = client.create_folder(folder_path)

    assert response.status_code == 201, (
        f"Не удалось создать тестовую папку: "
        f"{response.status_code}, {response.text}"
    )

    yield folder_path

    response = client.delete_resource(folder_path)

    assert response.status_code in (204, 202, 404), (
        f"Не удалось удалить тестовую папку: "
        f"{response.status_code}, {response.text}"
    )
