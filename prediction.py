import pandas as pd
from src.logger import logging
from src.exception import CustomException
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import sys
import os
import pickle



def prediction(inputs):
    try:
        logging.info("In Predict py importing models")
        preprocessor = pickle.load(open(os.path.join("artifacts","preprocessor.pkl"),"rb"))
        model = pickle.load(open(os.path.join("artifacts","model.pkl"),"rb"))
        
        classNames = ['ssc_p', 'ssc_b', 'hsc_p', 'hsc_b', 'hsc_s',
        'degree_p', 'degree_t', 'workex', 'etest_p', 'specialisation',
        'mba_p']
        
        logging.info("Data Transoformation")
        data = pd.DataFrame([inputs],columns=classNames)
        logging.info("Predicting Results")
        data = preprocessor.transform(data)
        result = model.predict(data)
        if result[0]==0:
            logging.info(f"Result is {result[0]}")
            return 0
        else:
            logging.info(f"Result is {result[0]}")
            return 1
        

        
    except Exception as e:
        logging.info(CustomException(e,sys))
        raise CustomException(e,sys)

if __name__ == "__main__":
    inputs = [52.58, "Others", 54.6, "Central", "Commerce", 50.2, "Comm&Mgmt", "Yes", 76.0, "Mkt&Fin", 65.33]
    result = prediction(inputs)
    print(result)
