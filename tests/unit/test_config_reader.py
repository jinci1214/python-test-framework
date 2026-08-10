import pytest

from utils.config_reader import load_config


pytestmark = pytest.mark.unit


def test_load_config():
    config = load_config()

    assert config["base_url"] == "https://the-internet.herokuapp.com"
    assert config["username"] == "tomsmith"
    assert config["password"] == "SuperSecretPassword!"


def test_load_config_does_not_depend_on_working_directory(
    tmp_path,
    monkeypatch
):
    monkeypatch.chdir(tmp_path)

    config = load_config()

    assert "base_url" in config

def test_environment_variables_override_yaml(monkeypatch):
    monkeypatch.setenv(
        "TEST_BASE_URL",
        "https://test.example.com"
    )
    monkeypatch.setenv(
        "TEST_USERNAME",
        "environment-user"
    )
    monkeypatch.setenv(
        "TEST_PASSWORD",
        "environment-password"
    )

    config = load_config()

    assert config["base_url"] == "https://test.example.com"
    assert config["username"] == "environment-user"
    assert config["password"] == "environment-password"
