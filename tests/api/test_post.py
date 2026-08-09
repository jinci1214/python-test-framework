import requests
import pytest

pytestmark = pytest.mark.api

def test_post_json():
    url = "https://postman-echo.com/post"

    data = {
        "username": "wuyi",
        "password": "123456"
    }

    response = requests.post(
        url,
        json=data,
        timeout=10
    )

    print(response.status_code)

    result = response.json()
    print(result)

    assert response.status_code == 200

    assert result["json"]["username"] == "wuyi"