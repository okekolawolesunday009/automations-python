import logging
import os


LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "app.log")


os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

def get_logger(name):
    return logging.getLogger(name)

def log_message(message):
    logger = get_logger("app_logger")
    logger.info(message)