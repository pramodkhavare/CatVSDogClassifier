from CNNClassifier.components.ingestion import DataIngestion 
from CNNClassifier.config.configuration import DataIngestionConfig,ConfigurationManager

config = ConfigurationManager()
data_ingestion_config = config.get_data_ingestion_config()
data_ingestion = DataIngestion(config=data_ingestion_config)
data_ingestion.download_file()
data_ingestion.unzip_and_clean()

# D:\Data Science\Deep Learning\Project\CatvsDogClassifier\src\CNNClassifier\pipeline\stag1.py