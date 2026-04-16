import logging
import os
from datetime import datetime

log_path = os.path.join(os.getcwd(), "logs")
os.makedirs(log_path,exist_ok=True)

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d')}.log"
LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format= "[ %(asctime)s ] [ %(levelname)s ] [ %(name)s ] [ line: %(lineno)d ][file: %(filename)s] - %(message)s",
    level=logging.INFO
)