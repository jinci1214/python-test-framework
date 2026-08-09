from pathlib import Path

import yaml


CONFIG_PATH = (
    Path(__file__).resolve().parent.parent
    / "config"
    / "config.yaml"
)


def load_config():
    with CONFIG_PATH.open(
        "r",
        encoding="utf-8"
    ) as config_file:
        return yaml.safe_load(config_file)