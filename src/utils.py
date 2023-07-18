import os
import sys
from src.logger import logging
from src.exception import CustmerExcepetion

sys.path.append(r"D:\Modular coding End to end\ml_pipeline_project")

import pickle

def save_obj(file_path , obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path , exist_ok=True)

        with open(file_path , "wb") as file_obj:
            pickle.dump(obj , file_obj)

    except Exception as e:
        raise CustmerExcepetion(e, sys)