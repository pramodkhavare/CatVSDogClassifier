from CNNClassifier.constant import PARAM_FILE_PATH ,CONFIG_FILE_PATH
import os 
import urllib.request as request 
from zipfile import ZipFile 
from CNNClassifier.logger import logging 
from pathlib import Path 
import tqdm as tqdm
from CNNClassifier.config.configuration import ConfigurationManager
from CNNClassifier.exception import CustomException 
import os ,sys

class DataIngestion :
    def __init__(self ,config:ConfigurationManager):
        self.config = config 

    def download_file(self):
        try:
            if not os.path.exists(self.config.local_data_file):
                filenmae , url = request.urlretrieve(
                    url=self.config.source_URL ,
                    filename= self.config.local_data_file
                ) 
        except Exception as e:
            logging.info(f'Unable to Donload file {self.config.local_data_file}')
            raise CustomException(e,sys)

    def get_updated_list_of_file(self ,list_of_files):
        updated_list_of_file = [f for f in list_of_files if f.endswith('.jpg') and ("cat" or "dog" in f) ]
        return updated_list_of_file 
    

    
    def preprocess(self ,zf:ZipFile ,f:str ,working_dir :str):
        target_filepath =os.path.join(working_dir ,f)
        if not os.path.exists(target_filepath):
            zf.extract(f ,working_dir)

        if os.path.getsize == 0:
            os.remove(target_filepath)        



    def unzip_and_clean(self):
        with ZipFile(file=self.config.local_data_file , mode='r') as zf:
            list_of_file = zf.namelist()
            updated_list_of_file = self.get_updated_list_of_file(list_of_files=list_of_file)

            for f in updated_list_of_file :
                self.preprocess(f=f ,zf=zf ,working_dir=self.config.unzip_dir)



# D:\Deep Learning\CatvsDogClassifier\src\CNNClassifier\components\data_ingestion.py
    
    