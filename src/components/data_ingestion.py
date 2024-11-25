import os
import sys
sys.path.append("/Users/kewaldharamshi/Documents/CODING/PYTHON/PROJECTS/ML projects/Student Preditction")

from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "raw.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig() 
        
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            # Read the dataset
            df = pd.read_csv('notebook /data/stud.csv')
            logging.info('Read the dataset as dataframe')
            
            # Create artifacts directory if it doesn't exist
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            
            # Save the raw dataset
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            
            logging.info("Train-test split initiated")
            
            # Split the dataset into training and testing sets
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            
            # Save the split datasets
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            
            logging.info("Ingestion of the data completed")
            
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )
        except Exception as e:
            raise CustomException(e, sys)
        
if __name__ == "__main__":
    obj = DataIngestion()
    train_data,test_data = obj.initiate_data_ingestion()  # Call the method to initiate data ingestion
    
    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_data,test_data)
