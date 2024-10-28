from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.prepare_base_model import PrepareBaseModel
from src.cnnClassifier import logger

STAGE_NAME = 'Prepare base model'

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass
        
    def main(self):
        try:
            config = ConfigurationManager()
            prepare_base_model_config = config.get_prepare_base_model_config()
            prepare_base_mode = PrepareBaseModel(config=prepare_base_model_config)
            prepare_base_mode.get_base_model()
            prepare_base_mode.update_base_model()
        except Exception as e:
            raise e
        
if __name__ == "__main__":
    try:
        logger.info(f">>> Stage {STAGE_NAME} started <<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>> Stage {STAGE_NAME} Completed. <<<")
    except Exception as e:
        raise e