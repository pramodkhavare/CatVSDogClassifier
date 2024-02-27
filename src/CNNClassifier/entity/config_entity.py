from dataclasses import dataclass 
import os ,sys 
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir :Path 
    source_URL : str 
    local_data_file :Path 
    unzip_dir :Path

@dataclass(frozen=True)
class PrepareModelConfig:
    root_dir :Path 
    base_model_path :Path 
    updated_base_model_path :Path 
    augmentation :str
    params_image_size : list 
    params_learning_rate :float 
    params_include_top : bool 
    params_weights : str 
    params_classes : int
    
@dataclass(frozen=True)
class PrepareCallbacksConfig:
    root_dir :Path 
    tensorboard_root_log_dir :Path 
    checkpoint_model_filepath :Path 

@dataclass(frozen=True)
class TrainingConfig:
    root_dir :Path 
    trained_model_path :Path 
    updated_base_model_path :Path 
    training_data :Path 
    param_batch_size : int 
    param_epochs : int
    param_is_augmentation : bool 
    param_image_size : list 


@dataclass(frozen=True)
class EvaluationConfig:
    path_of_model :Path 
    training_data :Path
    param_image_size : list
    param_batch_size : int
