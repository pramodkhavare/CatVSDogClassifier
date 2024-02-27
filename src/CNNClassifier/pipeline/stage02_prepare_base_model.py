import os ,sys 
from pathlib import Path 
from CNNClassifier.config.configuration import ConfigurationManager 
from CNNClassifier.components.prepare_base_model import PrepareBaseModel
from CNNClassifier.logger import logging 
from CNNClassifier.exception import CustomException
process = 'PrepareBaeModel'


def main():
    try:
        config = ConfigurationManager()
        base_model_config = config.get_prepare_basse_model_config()
        prepare_base_model = PrepareBaseModel(base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()
    except Exception as e:
        logging.info("Something wrong in {process} process")
        raise CustomException(e ,sys)

if __name__ == '__main__':
    main()