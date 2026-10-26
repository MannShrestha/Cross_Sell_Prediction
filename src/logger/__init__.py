import logging
import os
from datetime import datetime
from logging.handlers import RotatingFileHandler

# ------------------------------------------------------------------------------
# Configuration
# ------------------------------------------------------------------------------

LOG_DIR = "logs"
MAX_LOG_SIZE = 5 * 1024 * 1024  # 5 MB
BACKUP_COUNT = 3

# Create logs directory
os.makedirs(LOG_DIR, exist_ok=True)

# Log file name
LOG_FILE = os.path.join(
    LOG_DIR,
    f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
)

# ------------------------------------------------------------------------------
# Logger Configuration
# ------------------------------------------------------------------------------

def configure_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Prevent duplicate handlers
    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "[ %(asctime)s ] %(levelname)s - %(message)s"
    )

    # File Handler
    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=MAX_LOG_SIZE,
        backupCount=BACKUP_COUNT
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


# Initialize logger
logger = configure_logger()

