from CNNClassifier.components.data_ingestion import DataIngestion 
from CNNClassifier.config.configuration import ConfigurationManager 
from CNNClassifier.logger import logging
from CNNClassifier.exception import CustomException 
import os ,sys
# from CNNClassifier.utils.utils import get_size
process = 'DataIngestion'


def main():
    try:
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.unzip_and_clean()
    except Exception as e:
        logging.info("Something wrong in {process} process")
        raise CustomException(e ,sys)

if __name__ == '__main__':
    main()


