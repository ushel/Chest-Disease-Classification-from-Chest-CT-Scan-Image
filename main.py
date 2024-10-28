# create endpoint

from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.cnnClassifier.components.data_ingestion import DataIngestion
from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier import logger

STAGE_NAME = 'Data Ingestion Stage'

try:
    logger.info(f">>> Stage {STAGE_NAME} started <<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>> Stage {STAGE_NAME} completed <<<")
except Exception as e:
    logger.exception(e)
    raise e
    