import os 
import sys
sys.path.append(r"D:\Modular coding End to end\ml_pipeline_project")
import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import CustmerExcepetion
from dataclasses import dataclass
from sklearn.model_selection import train_test_split


@dataclass
class DataIngestionConfig:
    train_file_path = os.path.join("artifacts", "train.csv")
    test_file_path = os.path.join("artifacts", "test.csv")
    raw_file_path = os.path.join("artifacts", "raw.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def inititate_data_ingestion(self):
        try:
            data = pd.read_csv(os.path.join("data/", "adult.csv"))
            logging.info("Successfully read the data")
            
            # making dir
            os.mkdir(os.path.dirname(self.ingestion_config.raw_file_path))
            logging.info("Making folder...")

            # saving the csv file
            data.to_csv(self.ingestion_config.raw_file_path , index=False)
            logging.info("successfully save the data")
            
            train_set , test_set = train_test_split(data , test_size=0.2, random_state=42)
            logging.info("Successfully splitted data into train and split")

            train_set.to_csv(self.ingestion_config.train_file_path , index= False , header=True)
            test_set.to_csv(self.ingestion_config.test_file_path , index=False , header = True)

            logging.info("Data ingested successfully")
            return(
                self.ingestion_config.train_file_path,
                self.ingestion_config.test_file_path
            )

        except Exception as e:
            logging.info("Error occured in file name")
            raise CustmerExcepetion(e, sys)
        

if __name__ == "__main__":
    obj = DataIngestion()
    obj.inititate_data_ingestion()
        

