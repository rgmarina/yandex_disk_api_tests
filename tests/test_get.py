
def test_get_disk_info(client):
    response = client.get_disk_info()

    assert response.status_code == 200

    data = response.json()

    assert "total_space" in data
    assert "used_space" in data
    assert isinstance(data["total_space"], int)
    assert isinstance(data["used_space"], int)


def test_get_existing_folder(client, test_folder):
    response = client.get_resource(test_folder)

    assert response.status_code == 200

    data = response.json()

    assert data["type"] == "dir"
    assert data["path"] == test_folder


def test_get_nonexistent_folder(client, test_folder):
    nonexistent_path = f"{test_folder}/nonexistent"

    response = client.get_resource(nonexistent_path)

    assert response.status_code == 404

    data = response.json()

    assert "error" in data
