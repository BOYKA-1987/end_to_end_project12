import os
import pandas as pd
import numpy as np
from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.exception import customexception

import sys
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path

class DataIngestionConfig:
    raw_data_path:str=os.path.join("artifacts","raw.csv")
    train_data_path:str=os.path.join("artifacts","train.csv")
    test_data_path:str=os.path.join("artifacts","test.csv")






class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    



    def initiate_data_ingestion(self):
        logging.info("data ingestion started")


        try:
            data=pd.read_csv(Path(os.path.join("notebooks/data","gemstone.csv")))
            logging.info("i have read the data frame")

            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)),exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info("i have saved the raw data set in artifact folder")

            logging.into("here i have perform train test split")

            train_data,test_data=train_test_split(data,test_size=0.25)
            logging.info("train test split complited")
            train_data.to_csv(self.ingestion_config.train_data_path,index=False)
            test_data.to_csv(self.ingestion_config.test_data_path,index=False)

            logging.info("data ingestion part complited..")



        except Exception as e:
            logging.info("exception during occured at data ingestion stage")
            raise customexception(e,sys)
        

