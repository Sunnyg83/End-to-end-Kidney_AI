from pathlib import Path
from CNN_Classifier.utils.common import read_yaml, create_directories   
from CNN_Classifier.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(
        self,
        config_filepath: Path = Path("config/config.yaml"),
        params_filepath: Path = Path("params.yaml")):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        # Ensure artifacts_root exists in the config
        artifacts_root = self.config.get("artifacts_root", "artifacts")
        create_directories([artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        # Ensure data_ingestion exists in the config
        data_ingestion_config = self.config.get("data_ingestion", {})
        return DataIngestionConfig(**data_ingestion_config)