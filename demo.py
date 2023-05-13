## Batch Prediction
## training Pipeline

#from Segmentation import start_training_pipeline
from Segmentation import pipeline
from Segmentation.pipeline import batch_prediction

file_path = r"E:\Insurance-Prediction-Project-main\bank-additional-full.csv"
if __name__=="__main__":
    try:
        output = batch_prediction.start_batch_prediction(input_file_path=file_path)
        #output = start_training_pipeline()
        print(output)
        
    except Exception as e:
        print(e)


