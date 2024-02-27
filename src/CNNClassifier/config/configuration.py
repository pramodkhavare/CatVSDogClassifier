import os,sys
from CNNClassifier.utils.utils import read_yaml ,create_directory 
from CNNClassifier.entity.config_entity import DataIngestionConfig ,PrepareModelConfig ,PrepareCallbacksConfig ,TrainingConfig ,EvaluationConfig
from CNNClassifier.constant import PARAM_FILE_PATH ,CONFIG_FILE_PATH 
from CNNClassifier.exception import CustomException 
from CNNClassifier.logger import logging
class ConfigurationManager():
    """
    This classs will manage all classes from config_entity file
    and link them with config.yaml file
    """
    def __init__(self, param_file_path =PARAM_FILE_PATH ,config_file_path =CONFIG_FILE_PATH ) -> None:
        """
        self.config and self.param will help you to read .yaml  file where data related with 
        model is stored
        """
        self.config = read_yaml(config_file_path)  
        self.param = read_yaml(param_file_path)
        create_directory([self.config.artifacts_root])

    def get_data_ingestion_config(self):
        try:
            logging.info(" data ingestion config getting in ConfigurationManager class started")
            config = self.config.data_ingestion
            create_directory([config.root_dir])
            data_ingestion_config = DataIngestionConfig(
                root_dir =  config.root_dir,
                source_URL= config.source_URL,
                local_data_file = config.local_data_file,
                unzip_dir= config.unzip_dir
            )
            return data_ingestion_config

        except Exception as e:
            logging.info("Unable to define get_data_ingestion_config")
            raise CustomException(e,sys)
    

    def get_prepare_basse_model_config(self) :
        """This method will pass into PrepareBaseModel"""
        try:
            config =self.config.prepare_base_model

            create_directory([config.root_dir])


            prepare_base_model = PrepareModelConfig(
                root_dir=config.root_dir ,
                base_model_path= config.base_model_path ,
                updated_base_model_path= config.updated_base_model_path,
                augmentation =self.param.AUGMENTATION,
                params_image_size = self.param.IMAGE_SIZE ,
                params_learning_rate = self.param.LEARNING_RATE ,
                # batch_size =self.param.BATCH_SIZE ,
                params_include_top = self.param.INCLUDE_TOP,
                # epochs = self.param.EPOCHS ,
                params_classes = self.param.CLASSES ,
                params_weights = self.param.WEIGHTS 

            )
            return prepare_base_model

        except Exception  as e:
            logging.info('Unable to define get_prepare_basse_model_config')
            raise CustomException( e ,sys)
    
    def get_prapare_callbacks_config(self):
        """This method will pass into CallBacks"""
        try:
            config = self.config.prepare_callbacks
            model_checkpoint_dir = os.path.dirname(config.checkpoint_model_filepath)
            create_directory([
                config.tensorboard_log_dir ,
                model_checkpoint_dir
            ])

            prepare_callback = PrepareCallbacksConfig(
                root_dir= config.root_dir ,
                tensorboard_log_dir= config.tensorboard_log_dir ,
                checkpoint_model_filepath = config.checkpoint_model_filepath
            )
            return prepare_callback

        except Exception  as e:
            logging.info('Unable to define get_prapare_callbacks_config')
            raise CustomException( e ,sys)
        


    def get_training_config(self):
        """This method will pass into Training class  """
        try:
            config = self.config.training 
            create_directory([config.root_dir])
            training_data_path =os.path.join(self.config.data_ingestion.unzip_dir,"PetImages")

            training_config = TrainingConfig(
                root_dir= config.root_dir ,
                trained_model_path= config.trained_model_path  , 
                updated_base_model_path= self.config.prepare_base_model.updated_base_model_path ,
                training_data = training_data_path ,
                param_epochs =  self.param.EPOCHS ,
                param_batch_size= self.param.BATCH_SIZE  ,
                param_is_augmentation= self.param.AUGMENTATION , 
                param_image_size= self.param.IMAGE_SIZE
                )
            
            return training_config
            

        except Exception  as e:
            logging.info('Unable to get get_training_config function')
            raise CustomException( e ,sys)
        

    def get_validation_config(self):
        try:
            eval_config =  EvaluationConfig(
                path_of_model= self.config.training.trained_model_path ,
                training_data= self.config.data_ingestion.unzip_dir ,
                param_image_size = self.param.IMAGE_SIZE ,
                param_batch_size = self.param.BATCH_SIZE 
            )

            return eval_config

        except Exception  as e:
            logging.info('Unable to get get_validation_config')
            raise CustomException( e ,sys)

from pathlib import Path



        

