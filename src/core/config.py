#读取配置文件
import yaml
from pathlib import Path

def load_config():
    config_path = Path(__file__).parent.parent.parent / "config" / "settings.yaml"
    with open(config_path, "r") as f:
        return yaml.safe_load(f)

config = load_config()