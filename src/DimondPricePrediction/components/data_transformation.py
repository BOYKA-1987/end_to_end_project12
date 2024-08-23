import os
import sys
import pandas as pd
import numpy as np


from dataclasses import dataclass
from src.DimondPricePrediction.exception import customexception
from src.DimondPricePrediction.logger import logging

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder,StandardScaler
 
from src.DimondPricePrediction.utils.utils import save_object


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join("artifacts","preprocessor.pkl")




class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()




    def get_data_transformation(self):
    
        try:


            pass
        except Exception as e:
            logging.info("Exception occured in the initiate_datatransformation")

            raise customexception(e,sys)

    
    def initiate_data_transformation(self,train_path,test_path):




        try:

            pass
        except Exception as e:
            logging.info("Exception occured in the initiate_datatransformation")

            raise customexception(e,sys)



