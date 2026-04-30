import logging
from pathlib import Path

APP_DIR = Path(__file__).resolve().parent
LOG_DIR = APP_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)


def setup_logging() -> None:
    logging.basicConfig(
        filename=LOG_DIR / "stylmoda_production.log",
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        encoding="utf-8",
    )
    logging.info("StylModa v3 production logging started")
