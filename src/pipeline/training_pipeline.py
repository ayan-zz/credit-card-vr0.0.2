from src.components.data_ingestion import dataingestion
from src.components.data_transformation import DataTransformation
from src.components.model_training import modeltrainer


if __name__=="__main__":
    obj=dataingestion()
    train_data,test_data=obj.initiate_data_ingestion()

    obj_trans=DataTransformation()
    train_arr,test_arr,_=obj_trans.initiate_data_trasformation(train_data,test_data)

    obj_model=modeltrainer()
    print(obj_model.initiate_model_training(train_arr,test_arr))
