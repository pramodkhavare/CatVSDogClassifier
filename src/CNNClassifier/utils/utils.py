from CNNClassifier.logger import logging 
from CNNClassifier.exception import CustomException 
import os ,sys 
from pathlib import Path 
from ensure import ensure_annotations
from box import ConfigBox
import yaml as yaml

@ensure_annotations
def read_yaml(path_to_yaml :Path):
    """Code will run yaml file 
    args ==1] path_to_yaml :-path where your yaml file stored 
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            return ConfigBox(content) 
    except Exception as e:
        logging.info(f"Unable to read yaml file{path_to_yaml}")
        raise CustomException(e ,sys)

@ensure_annotations
def create_directory(path_to_directory:list ,verbose=True):
    """Code will help to create directory"""
    try:
        for path in path_to_directory:
            os.makedirs(path ,exist_ok=True)
            if verbose:
                logging.info(f"Creted directory at {path}")
        
    except Exception as e:
        logging.info(f"Unable to create new directory {path_to_directory}")
        raise CustomException(e ,sys)
    

# @ensure_annotations
# def get_size(path: Path) -> str:
#     size_in_kb = round(os.path.getsize(path)/1024)
#     return f"~ {size_in_kb} KB"


@ensure_annotations
def save_json():
    pass 

@ensure_annotations
def load_json():
    pass

@ensure_annotations
def save_model():
    pass 

@ensure_annotations
def load_model():
    pass 
