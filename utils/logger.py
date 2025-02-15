# utils/logger.py

import logging
import os

LOG_FILE = "logs/system.log"

# Ensure the logs directory exists
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def log_event(event: str):
    """
    Logs an event in the system.

    Args:
        event (str): The event description.
    """
    logging.info(event)
    print(event)  # Also print to console for real-time feedback
