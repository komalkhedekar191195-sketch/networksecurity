from src.components.data_ingestion import DataIngestion
from src.exception.exception import NetworkSecurityException
from src.logging.logger import logging
from src.entity.config_entity import DataIngestionConfig
from src.entity.config_entity import TrainingPipelineConfig

import sys

if __name__=='__main__':
    try:
        trainingPipelineConfig =TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingPipelineConfig)
        data_ingestion= DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)

    except Exception as e:
        raise NetworkSecurityException(e, sys)