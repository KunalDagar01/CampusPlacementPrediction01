import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
from sklearn.model_selection import GridSearchCV
from src.logger import logging
from src.components.data_ingestion import data_ingestion
from src.pipelines.train_pipeline import trainPipeline
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from src.exception import CustomException
from imblearn.over_sampling import SMOTE
import pickle
import os
import sys


try:
    logging.info("At model trainier")
    raw_data_path  = os.path.join("artifacts","raw.csv")
    train_data_path,test_data_path = data_ingestion(raw_data_path)
    preprocessor,X_train,y_train,X_test,y_test = trainPipeline(train_data_path,test_data_path)

    logging.info("Splitting Sucess")
    logging.info(f'Got {X_test.columns} as column names')

    columnsNames = list(X_test.columns)
    with open(os.path.join("artifacts","columnNames.txt"),"w") as file:
         file.write(','.join(columnsNames))

    logging.info("Transforming data")

    X_train=pd.DataFrame(preprocessor.fit_transform(X_train),columns=preprocessor.get_feature_names_out())
    X_test=pd.DataFrame(preprocessor.transform(X_test),columns=preprocessor.get_feature_names_out())

    logging.info(f"{X_train.head()}")

    logging.info("Doing hyperparameter tuning for SVC Classifier")
    pickle.dump(preprocessor, open(os.path.join("artifacts","preprocessor.pkl"), 'wb'))


    logging.info("Applying smote")
    smote = SMOTE()
    X_train,y_train = smote.fit_resample(X_train,y_train)

    logging.info(f"Got {X_train.shape} as new rows and columns")

    parameters = {
        "criterion":['gini','entropy'],
        "splitter":['best','random'],
        "max_depth":[1,2,3,4,5]
    }

    clf = GridSearchCV(DecisionTreeClassifier(),param_grid=parameters,cv=5,verbose=1)
    clf.fit(X_train,y_train)
    logging.info("Done hyperpamater tuning")
    model = DecisionTreeClassifier(
        criterion=clf.best_params_['criterion'],
        splitter= clf.best_params_['splitter'],
        max_depth=clf.best_params_['max_depth']

    )
    logging.info("Model Training")
    model.fit(X_train,y_train)

    logging.info("Training Success")
    y_pred = model.predict(X_test)
    score = accuracy_score(y_test,y_pred)
    cfr = classification_report(y_test,y_pred)
    cfm = confusion_matrix(y_test,y_pred)

    logging.info("Training success")
    logging.info(f"Accuracy is {score*100} %")
    logging.info(f"Classification report \n {cfr} ")
    logging.info(f"confusion matrix \n {cfm}")
    logging.info("saved model file at models")

    pickle.dump(model, open(os.path.join("artifacts","model.pkl"), 'wb'))

except Exception as e:
    logging.info(CustomException(e,sys))
    raise CustomException(e,sys)






