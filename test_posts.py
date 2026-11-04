import requests


def test_create_post(base_url):
    payload = {"title": "Мой пост", "body": "Текст", "userId": 1}
    response = requests.post(
        f"{base_url}/posts",
        json=payload,
        timeout=10,
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["userId"] == payload["userId"]
    assert "id" in data


def test_update_post(base_url):
    payload = {"id": 1, "title": "Мой пост", "body": "Текст", "userId": 1}
    response = requests.put(
        f"{base_url}/posts/1",
        json=payload,
        timeout=10,
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["id"] == payload["id"]


def test_delete_post(base_url):
    response = requests.delete(
        f"{base_url}/posts/1",
        timeout=10,
    )
    assert response.status_code == 200
    assert response.json() == {}
