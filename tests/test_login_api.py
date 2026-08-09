from api.login_api import LoginAPI
from utils.logger import get_logger
import pytest

pytestmark = pytest.mark.api

logger = get_logger()


def test_login_api():

    print()
    logger.info("开始登录测试")

    api = LoginAPI()

    response = api.login(
        "wuyi",
        "123456"
    )

    logger.info(
        f"响应状态码:{response.status_code}"
    )

    assert response.status_code == 200

    logger.info("登录测试成功")