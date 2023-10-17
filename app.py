from flask import Flask, request, render_template
import pandas as pd
import pickle
from src.logger import logging
from src.exception import CustomException
from prediction import prediction
import sys
import os
import time

try:
    logging.info("In App.py")
    app = Flask(__name__)

    logging.info("Showing Index page")
    @app.route('/')
    def index():
        return render_template('index.html')

    
    @app.route('/submit',methods=['GET','POST'])
    def submit():
        logging.info("Submit command recieved")
        start = time.time()
        if request.method=="POST":
            
            ssc_p = float(request.form.get('ssc_p'))
            ssc_b = request.form.get('ssc_b')
            hsc_p = float(request.form.get('hsc_p'))
            hsc_b = request.form.get('hsc_b')
            hsc_s = request.form.get('hsc_s')
            degree_p = float(request.form.get('degree_p'))
            degree_t = request.form.get('degree_t')
            workex = request.form.get('workex')
            etest_p = float(request.form.get('etest_p'))
            specialisation = request.form.get('specialisation')
            mba_p = float(request.form.get('mba_p'))

            inputs = [ssc_p,ssc_b,hsc_p,hsc_b,hsc_s,degree_p,degree_t,workex,etest_p,specialisation,mba_p]
            logging.info(f"recieved values {inputs}")
            result = prediction(inputs)
            if(result==0):
                end = time.time()
                net = end - start
                logging.info("Done Prediction")
                logging.info(f"Took {net}seconds for execution")
                return render_template('index.html',prediction="Sorry but your chances for placement are Low")
            else:
                end = time.time()
                net = end - start
                logging.info("Done Prediction")
                logging.info(f"Took {net} seconds for execution")
                return render_template('index.html',prediction="Congratulations you will be placed")
            
            
            
    if __name__ == "__main__":
        app.run('0.0.0.0',port='8080')
except Exception as e:
    logging.info(CustomException(e,sys))
    raise CustomException(e,sys)