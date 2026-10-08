
def test_create_folder(client, test_folder):
    new_folder = f"{test_folder}/new_folder"

    response = client.create_folder(new_folder)

    assert response.status_code == 201

    get_response = client.get_resource(new_folder)

    assert get_response.status_code == 200
    assert get_response.json()["type"] == "dir"
    assert get_response.json()["path"] == new_folder


def test_create_existing_folder(client, test_folder):
    response = client.create_folder(test_folder)

    assert response.status_code == 409

    data = response.json()

    assert "error" in data
