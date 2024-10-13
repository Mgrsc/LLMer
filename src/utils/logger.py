import os
import logging
from pathlib import Path
from logging.handlers import RotatingFileHandler
from config import logging_enabled, log_dir
import uvicorn

def setup_logging():
    logger = logging.getLogger('app')

    # Clear existing handlers, if any
    logging.getLogger().handlers = [] # Clear root logger handlers
    logger.handlers = []

    if not logging_enabled:
        logger.addHandler(logging.NullHandler())
    else:
        Path(log_dir).mkdir(parents=True, exist_ok=True)
        log_file_path = Path(log_dir) / 'app.log'

        logger.setLevel(logging.INFO)

        if not logger.handlers:
            file_handler = RotatingFileHandler(
                log_file_path, maxBytes=10*1024*1024, backupCount=5, encoding='utf-8'
            )
            file_handler.setLevel(logging.INFO)

            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)

            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)

            logger.addHandler(file_handler)
            logger.addHandler(console_handler)

    return logger

# Create a global logger instance
logger = setup_logging()

