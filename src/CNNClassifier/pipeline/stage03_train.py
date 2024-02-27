from CNNClassifier.logger import logging
from CNNClassifier.exception import CustomException
import os ,sys
from CNNClassifier.config.configuration import ConfigurationManager 
from CNNClassifier.components.train1 import Training
process = 'Training Model'


def main():
    try:
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()
    except Exception as e:
        logging.info("Something wrong in {process} process")
        raise CustomException(e ,sys)

if __name__ == '__main__':
    main()




