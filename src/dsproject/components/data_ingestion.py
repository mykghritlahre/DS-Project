import os # to create directories for raw and ingested data
import sys # to get exception details
from src.dsproject.logger import logging # logging 
from src.dsproject.exception import CustomException # to implement custom exceptions
import pandas as pd   # since this script will be dealing with dataframes 

from dataclasses import dataclass # so we can initialise our input parameters

@dataclass
class DataIngestionConfig:
    train_data_path :str = os.path.join('artifacts','train.csv')
    test_data_path :str = os.path.join('artifacts','test.csv')
    raw_data_path :str = os.path.join('artifacts','raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    
    def initiate_data_ingestion(self):
        try:
            ##reading code
            logging.info("Reading from mysql database")

            ##need to create folder
        except Exception as e:
            raise CustomException(e, sys)
