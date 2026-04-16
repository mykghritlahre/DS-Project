from src.dsproject.logger import logging
from src.dsproject.exception import CustomException
import sys

if __name__ == "__main__":
    logging.info("Starting the application...")

    try:
        # Simulating an error
        a = 1 / 0
    except Exception as e:
        logging.error("Custom exception")
        raise CustomException(e, sys)