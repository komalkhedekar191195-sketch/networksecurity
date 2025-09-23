from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.components.data_transformation import DataTransformation
from src.exception.exception import NetworkSecurityException
from src.logging.logger import logging
from src.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig
from src.entity.config_entity import TrainingPipelineConfig
from src.components.model_trainer import ModelTrainer

import sys

if __name__=='__main__':
    try:
        trainingPipelineConfig =TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingPipelineConfig)
        data_ingestion= DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        logging.info("Data initiation completed")
        print(dataingestionartifact)
        data_validation_config= DataValidationConfig(trainingPipelineConfig)
        data_validation = DataValidation(dataingestionartifact, data_validation_config)
        logging.info("Initiate the data validation")
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("Data validation completed")
        print(data_validation_artifact)
        data_transformation_config= DataTransformationConfig(trainingPipelineConfig)
        logging.info("Data transformation started")
        data_transformation= DataTransformation(data_validation_artifact, data_transformation_config)
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info("Data transformation completed")

        logging.info("Model Training started")
        model_trainer_config = ModelTrainerConfig(trainingPipelineConfig)
        model_trainer = ModelTrainer(model_trainer_config = model_trainer_config, data_transformation_artifact= data_transformation_artifact)
        model_trainer_artifact = model_trainer.initiate_model_trainer()
       

    except Exception as e:
        raise NetworkSecurityException(e, sys)