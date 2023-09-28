import pandas as pd
import numpy as np
import os,sys
import warnings
warnings.filterwarnings('ignore')
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier
from xgboost import XGBClassifier
from sklearn.metrics import f1_score,accuracy_score
from src.utils import evaluate_models,save_object
from src.logging import logging
from src.exception import CustomException
from dataclasses import dataclass

@dataclass
class ModeltrainerConfig:
    model_path=os.path.join('artifact','model.pkl')
class modeltrainer:
    def __init__(self):
        self.modeltrainer_obj=ModeltrainerConfig()
    def initiate_model_training(self,train_array,test_array):
        try:
            logging.info('Iniate model training')
            X_train,y_train,X_test,y_test=(train_array[:,:-1],train_array[:,-1],
                                           test_array[:,:-1],test_array[:,-1])
            
            models={'logisticRegression': LogisticRegression(),
                    #'GradientBoosting': GradientBoostingClassifier(),
                    'RandomForest': RandomForestClassifier(),
                    'xgboost': XGBClassifier()
            }
            params={'logisticRegression':{'max_iter':[1000]}, 

                    #'GradientBoosting':{'n_estimators' :[10, 100, 1000],
                                        #'learning_rate' : [0.001, 0.01, 0.1],
                                        #'subsample' : [0.5, 0.7, 1.0],
                                        #'max_depth' : [3, 7, 9]},
                    'RandomForest':{'n_estimators': [8,16,32,64],'max_features':['sqrt','log2']},
                    'xgboost':{'n_estimators': [16,48,72,96], 'learning_rate':[0.01,0.01],'max_depth':[3]}}
            
            model_report:dict=evaluate_models(X_train=X_train,y_train=y_train,
                                             X_test=X_test,y_test=y_test,models=models,param=params)
            
            best_model_score = max(sorted(model_report.values()))

            best_model_name=list(model_report.keys())[list(model_report.values()).index(best_model_score)]
            best_model=models[best_model_name]

            save_object(
                file_path=self.modeltrainer_obj.model_path,
                obj=best_model)
            
            predicted=best_model.predict(X_test)

            fScore= f1_score(y_test,predicted)
            print(fScore)
            return (best_model_name,fScore)
            
        except Exception as e:
            raise CustomException(e,sys)

