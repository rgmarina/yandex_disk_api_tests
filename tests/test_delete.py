
import time


def test_delete_existing_folder(client, test_folder):
    folder_to_delete = f"{test_folder}/folder_to_delete"

    create_response = client.create_folder(folder_to_delete)

    assert create_response.status_code == 201, (
        f"Ошибка создания папки: "
        f"{create_response.status_code}, "
        f"{create_response.text}"
    )

    delete_response = client.delete_resource(folder_to_delete)

    assert delete_response.status_code in (204, 202), (
        f"Ошибка удаления: "
        f"{delete_response.status_code}, "
        f"{delete_response.text}"
    )

    deadline = time.monotonic() + 30

    while time.monotonic() < deadline:
        get_response = client.get_resource(folder_to_delete)

        if get_response.status_code == 404:
            return

        assert get_response.status_code == 200, (
            f"Неожиданный ответ: "
            f"{get_response.status_code}, "
            f"{get_response.text}"
        )

        time.sleep(1)

    raise AssertionError(
        "Папка не была удалена за 30 секунд"
    )


def test_delete_nonexistent_folder(client, test_folder):
    nonexistent_folder = f"{test_folder}/does_not_exist"

    response = client.delete_resource(nonexistent_folder)

    assert response.status_code == 404, (
        f"Ожидался статус 404, "
        f"но получен {response.status_code}: "
        f"{response.text}"
    )

    data = response.json()

    assert "error" in data
