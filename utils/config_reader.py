import os
from pathlib import Path

import yaml


CONFIG_PATH = (
    Path(__file__).resolve().parent.parent
    / "config"
    / "config.yaml"
)

ENVIRONMENT_OVERRIDES = {
    "TEST_BASE_URL": "base_url",
    "TEST_USERNAME": "username",
    "TEST_PASSWORD": "password",
}


def load_config():
    with CONFIG_PATH.open(
        "r",
        encoding="utf-8"
    ) as config_file:
        config = yaml.safe_load(config_file)

    for environment_name, config_name in ENVIRONMENT_OVERRIDES.items():
        environment_value = os.getenv(environment_name)

        if environment_value is not None:
            config[config_name] = environment_value

    return config