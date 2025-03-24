import sys
from pathlib import Path

# Add the `src` directory to the PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))

from CNN_Classifier import logger
from CNN_Classifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    pipeline = DataIngestionPipeline()
    pipeline.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=======================x")
except Exception as e:
    logger.exception(e)
    raise e