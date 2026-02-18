from src.KidneyTumorSegmentation import logger
from src.KidneyTumorSegmentation.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.KidneyTumorSegmentation.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline


STAGE_NAME = "DATA INGESTION STAGE"
try:
    logger.info(f">>>>>>>> stage{STAGE_NAME} started <<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "PREPARE BASE MODEL STAGE"

try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e