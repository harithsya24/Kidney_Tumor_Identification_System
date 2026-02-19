from src.KidneyTumorSegmentation import logger
from src.KidneyTumorSegmentation.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.KidneyTumorSegmentation.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.KidneyTumorSegmentation.pipeline.stage_03_model_training import ModelTrainingPipeline
from src.KidneyTumorSegmentation.pipeline.stage_04_model_evaluation import ModelEvaluationPipeline

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
    
STAGE_NAME = "MODEL TRAINING STAGE"

try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "MODEL EVALUATION STAGE"

try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e