import sys,os
import pandas as pd
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join('artifact','model.pkl')
            preprocessor_path=os.path.join('artifact','preprocessor.pkl')
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
              raise CustomException(e,sys)
class CustomData:
    def __init__(self, 
                 ID : int,
                 LIMIT_BAL :float,
                 SEX: int,
                 EDUCATION: int,
                 MARRIAGE: int,
                 AGE: int,
                 PAY_0: float,
                 PAY_2: float,
                 PAY_3: float,
                 PAY_4: float,
                 PAY_5: float,
                 PAY_6: float,
                 BILL_AMT1: float,
                 BILL_AMT2:float,
                 BILL_AMT3:float,
                 BILL_AMT4:float,
                 BILL_AMT5:float, 
                 BILL_AMT6:float,
                 PAY_AMT1:float,
                 PAY_AMT2:float,
                 PAY_AMT3:float,
                 PAY_AMT4:float,
                 PAY_AMT5:float,
                 PAY_AMT6:float
                 ):
                
                self.ID =ID 
                self.LIMIT_BAL = LIMIT_BAL
                self.SEX = SEX
                self.EDUCATION = EDUCATION
                self.MARRIAGE=MARRIAGE
                self.AGE=AGE
                self.PAY_0=PAY_0
                self.PAY_2 = PAY_2
                self.PAY_3= PAY_3
                self.PAY_4= PAY_4
                self.PAY_5=PAY_5
                self.PAY_6=PAY_6
                self.BILL_AMT1=BILL_AMT1
                self.BILL_AMT2=BILL_AMT2
                self.BILL_AMT3=BILL_AMT3
                self.BILL_AMT4=BILL_AMT4
                self.BILL_AMT5=BILL_AMT5
                self.BILL_AMT6=BILL_AMT6
                self.PAY_AMT1=PAY_AMT1
                self.PAY_AMT2=PAY_AMT2
                self.PAY_AMT3=PAY_AMT3
                self.PAY_AMT4=PAY_AMT4
                self.PAY_AMT5=PAY_AMT5
                self.PAY_AMT6=PAY_AMT6
               
                
    def get_data_as_dataframe(self):
          try:
                custom_data_input_dict={
                      "ID":[self.ID], "LIMIT_BAL":[self.LIMIT_BAL],
                      "SEX":[self.SEX],"EDUCATION":[self.EDUCATION],
                      "MARRIAGE":[self.MARRIAGE],"AGE":[self.AGE],
                      "PAY_0":[self.PAY_0],"PAY_2":[self.PAY_2],"PAY_3":[self.PAY_3],
                      "PAY_4":[self.PAY_4],"PAY_5":[self.PAY_5],"PAY_6":[self.PAY_6],
                      "BILL_AMT1":[self.BILL_AMT1],"BILL_AMT2":[self.BILL_AMT2],"BILL_AMT3":[self.BILL_AMT3],
                      "BILL_AMT4":[self.BILL_AMT4],"BILL_AMT5":[self.BILL_AMT5],"BILL_AMT6":[self.BILL_AMT6],
                      "PAY_AMT1":[self.PAY_AMT1],"PAY_AMT2":[self.PAY_AMT2],"PAY_AMT3":[self.PAY_AMT3],
                      "PAY_AMT4":[self.PAY_AMT4],"PAY_AMT5":[self.PAY_AMT5],"PAY_AMT6":[self.PAY_AMT6]           
                }
                return pd.DataFrame(custom_data_input_dict)
          
          except Exception as e:
                raise CustomException(e,sys)
          