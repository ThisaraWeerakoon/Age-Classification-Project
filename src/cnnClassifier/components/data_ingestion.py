import os
import urllib.request as request
import zipfile
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        self.data_ingestion_config = data_ingestion_config

    def download_file(self):
        os.makedirs(os.path.dirname(self.data_ingestion_config.local_data_file), exist_ok=True)

        if not os.path.exists(self.data_ingestion_config.local_data_file):
            #print(self.data_ingestion_config.source_URL)
            #print(self.data_ingestion_config.local_data_file)
            filename,headers = request.urlretrieve(
                url=self.data_ingestion_config.source_URL,
                filename=self.data_ingestion_config.local_data_file
            )
            logger.info(f"{filename} download with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.data_ingestion_config.local_data_file))}")


    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function return None
        """

        unzip_path = self.data_ingestion_config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.data_ingestion_config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            logger.info(f"Zip file extracted to: {unzip_path}")