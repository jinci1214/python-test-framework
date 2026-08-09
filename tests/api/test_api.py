import requests
import pytest

pytestmark = pytest.mark.api

def test_get_baidu():
    response = requests.get("https://www.baidu.com")

    print(response.status_code)

    assert response.status_code == 200