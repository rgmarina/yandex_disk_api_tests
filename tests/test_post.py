
import time


def test_copy_folder(client, test_folder):
    source_folder = f"{test_folder}/source_folder"
    copied_folder = f"{test_folder}/copied_folder"

    create_response = client.create_folder(source_folder)

    assert create_response.status_code == 201

    copy_response = client.copy_resource(
        source_folder,
        copied_folder,
    )

    assert copy_response.status_code in (201, 202), (
        f"Ошибка копирования: "
        f"{copy_response.status_code}, "
        f"{copy_response.text}"
    )

    deadline = time.monotonic() + 30

    while time.monotonic() < deadline:
        get_response = client.get_resource(copied_folder)

        if get_response.status_code == 200:
            data = get_response.json()

            assert data["type"] == "dir"
            assert data["path"] == copied_folder
            return

        assert get_response.status_code == 404, (
            f"Неожиданный ответ: "
            f"{get_response.status_code}, "
            f"{get_response.text}"
        )

        time.sleep(1)

    raise AssertionError(
        "Скопированная папка не появилась за 30 секунд"
    )
