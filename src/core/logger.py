#日志管理
import logging
from pathlib import Path
from src.core.config import config

log_file = Path(__file__).parent.parent.parent / config["logging"]["file"]
logging.basicConfig(
    level=config["logging"]["level"],
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)