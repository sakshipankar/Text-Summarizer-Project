import os
import sys
import logging

# Define log format
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Define log file location
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")

# Create logs directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

# Define logger
logger = logging.getLogger("textSummarizationLogger")
