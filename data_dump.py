import pymongo
import pandas as pd
import json

client = pymongo.MongoClient("mongodb+srv://BackOrderPropagation:shraddha123@cluster0.ydatbkn.mongodb.net/?retryWrites=true&w=majority")


DATA_FILE_PATH = (r"/config/Customer_Segmentation_/bank-additional-full.csv")
DATABASE_NAME = "CUSTOMERS"
COLLECTION_NAME = "CUSTOMERS_PROJECT"
 

if __name__ =="__main__":
    df = pd.read_csv(r"/config/Customer_Segmentation_/bank-additional-full.csv", sep=';')
    print(f"Rows and Columns: {df.shape}")

    df.reset_index(drop = True, inplace = True)
    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
    
    
    