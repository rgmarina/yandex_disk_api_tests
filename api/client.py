
import requests


class YandexDiskClient:
    BASE_URL = "https://cloud-api.yandex.net/v1/disk"

    def __init__(self, token):
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"OAuth {token}",
            "Accept": "application/json",
        })

    def get_disk_info(self):
        return self.session.get(
            self.BASE_URL,
            timeout=20,
        )

    def get_resource(self, path):
        return self.session.get(
            f"{self.BASE_URL}/resources",
            params={"path": path},
            timeout=20,
        )

    def create_folder(self, path):
        return self.session.put(
            f"{self.BASE_URL}/resources",
            params={"path": path},
            timeout=20,
        )

    def copy_resource(self, source_path, destination_path):
        return self.session.post(
            f"{self.BASE_URL}/resources/copy",
            params={
                "from": source_path,
                "path": destination_path,
                "overwrite": "false",
            },
            timeout=20,
        )

    def delete_resource(self, path):
        return self.session.delete(
            f"{self.BASE_URL}/resources",
            params={
                "path": path,
                "permanently": "true",
                "force_async": "false",
            },
            timeout=20,
        )

    def close(self):
        self.session.close()
