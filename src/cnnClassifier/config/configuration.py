from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml,create_directories
from cnnClassifier.entity.config_entity import (DataIngestionConfig)

class ConfigurationManager:
    def __init__(
    self,
    config_filepath = CONFIG_FILE_PATH,
    params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])
    
    def get_data_ingestion_config(self) ->DataIngestionConfig:
        self.config = self.config.data_ingestion
        print(self.config.root_dir)
        create_directories([self.config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir = self.config.root_dir,
            source_URL = self.config.source_URL,
            local_data_file = self.config.local_data_file,
            unzip_dir = self.config.unzip_dir
        )

        return data_ingestion_config