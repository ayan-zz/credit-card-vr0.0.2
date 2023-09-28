import pandas as pd
import numpy as np
import os,sys
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from src.utils import save_object
from src.logging import logging
from src.exception import CustomException
from dataclasses import dataclass

@dataclass
class DataTransformationConfig:
    pre_processor_obj_path=os.path.join('artifact','preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.datatransformation_config=DataTransformationConfig()
    def get_transformation_obj(self):
        try:
            logging.info('Transformer object initialization started')

            numerical_col=['LIMIT_BAL', 'AGE', 'PAY_0', 'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6', 
                    'BILL_AMT1', 'BILL_AMT2', 'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6',
                    'PAY_AMT1', 'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6']
            #categorical_col=['SEX','EDUCATION', 'MARRIAGE']

            numerical_pipeline=Pipeline(steps=[('imputer',SimpleImputer(strategy='median'))
                                               ])
            #categorical_pipeline=Pipeline(steps=[('imputer',SimpleImputer(strategy='most_frequent')),
            #                                    ('encoder',OneHotEncoder())
            #                                    ])
            preprocessor=ColumnTransformer([("numerical_pipeline",numerical_pipeline,numerical_col)])
            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)


    def initiate_data_trasformation(self,train_path,test_path):
        try:
            logging.info('data transformation started')
            df_train=pd.read_csv(train_path)
            df_test=pd.read_csv(test_path)
            target_col_name='default payment next month'
            df_train.drop(index=3562, axis=0,inplace=True)
            print(df_train['default payment next month'].value_counts())
            print(df_test['default payment next month'].value_counts())

            logging.info('initializing preprocessor object') 

            preprocessor_obj=self.get_transformation_obj()

            df_train_col=df_train.columns[6:25]
            df_test_col=df_test.columns[6:25]
            #for col in df_train_col:
            #    df_train[col]=df_train[col].astype(float)
            df_train[df_train_col] = df_train[df_train_col].apply(pd.to_numeric, errors='coerce')
            df_test[df_test_col] = df_test[df_test_col].apply(pd.to_numeric, errors='coerce')
            #print(df_train['AGE'].head())
            #for col in df_test_col:
            #    df_test[col]=df_test[col].astype(float)
            
            
            others1=['0','4','5','6']
            df_train['EDUCATION']=df_train['EDUCATION'].replace(to_replace=others1,value='4')
            df_test['EDUCATION']=df_test['EDUCATION'].replace(to_replace=others1,value='4')
            
            
            others2=['0','3']
            df_train['MARRIAGE']=df_train['MARRIAGE'].replace(to_replace=others2,value='3')  
            df_test['MARRIAGE']=df_test['MARRIAGE'].replace(to_replace=others2,value='3')
            
            df_train['AGE']=df_train['AGE'].apply(pd.to_numeric, errors='coerce')
            df_train['LIMIT_BAL']=df_train['LIMIT_BAL'].apply(pd.to_numeric, errors='coerce')
            df_train['EDUCATION']=df_train['EDUCATION'].apply(pd.to_numeric, errors='coerce')
            df_train['MARRIAGE']=df_train['MARRIAGE'].apply(pd.to_numeric, errors='coerce')

            df_test['AGE']=df_test['AGE'].apply(pd.to_numeric, errors='coerce')
            df_test['LIMIT_BAL']=df_test['LIMIT_BAL'].apply(pd.to_numeric, errors='coerce')
            df_test['EDUCATION']=df_test['EDUCATION'].apply(pd.to_numeric, errors='coerce')
            df_test['MARRIAGE']=df_test['MARRIAGE'].apply(pd.to_numeric, errors='coerce')
           
            target_feature_train_df=df_train[target_col_name]
            target_feature_test_df=df_test[target_col_name]

            input_feature_train_df=df_train.drop(columns=['ID','default payment next month'],axis=1)
            input_feature_test_df=df_test.drop(columns=['ID','default payment next month'],axis=1)

            input_feature_train_arr=preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessor_obj.transform(input_feature_test_df)
            
            
            train_arr=np.c_[input_feature_train_arr,target_feature_train_df]
            test_arr=np.c_[input_feature_test_arr,target_feature_test_df]

            save_object(
                file_path=self.datatransformation_config.pre_processor_obj_path,
                obj=preprocessor_obj
            )
            logging.info('Applied preprocessor obj formed and saved')
            return (train_arr,test_arr,self.datatransformation_config.pre_processor_obj_path)

        except Exception as e:
            logging.info('error in the preprocessing stage')
            raise CustomException(e,sys)

