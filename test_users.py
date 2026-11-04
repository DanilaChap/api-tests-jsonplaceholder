import pytest
import requests


def test_get_user(base_url):
    response = requests.get(
        f"{base_url}/users/1",
        timeout=10,
    )
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "email" in data


def test_get_nonexistent_user(base_url):
    response = requests.get(
        f"{base_url}/users/999",
        timeout=10,
    )
    assert response.status_code == 404
    data = response.json()
    assert data == {}


def test_get_users_list(base_url):
    response = requests.get(
        f"{base_url}/users",
        timeout=10,
    )
    assert response.status_code == 200
    user_list = response.json()
    assert isinstance(user_list, list)
    assert len(user_list) == 10
    for user in user_list:
        assert "email" in user


@pytest.mark.parametrize(
    "user_id, expected_username",
    [
        (1, "Bret"),
        (2, "Antonette"),
        (3, "Samantha"),
    ],
)
def test_get_user_username(base_url, user_id, expected_username):
    response = requests.get(f"{base_url}/users/{user_id}", timeout=10)
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == expected_username
