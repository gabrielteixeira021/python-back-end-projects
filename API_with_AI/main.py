# Description: API integrated with ML model

# libraries import
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# load the model
try: 
    model = joblib.load("knn_iris_model.pkl")
    print("Model was successfully loaded")
except FileNotFoundError:
    print("Error: Model File 'knn_iris_model.pkl' was not found, certifies the 'train_model.py' was executed")
    model = None
    
# Defines the input's data structure
class IrisData(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
    
# Index mapping for class names
target_names = {
    0: 'setosa',
    1: 'versicolor',
    2: 'virginica'
} 

# Initializes fastAPI
app = FastAPI()

# Endpoint to root
@app.get("/")
def read_root():
    return {"message": "Iris Species Prediction. Access /docs to read the API documentation"}

# Endpoint to make the prediction
@app.post("/predict")
def predict_species(data: IrisData):
    if model is None:
        return {"error": "Model is unavailable. Please, check the server's log."}
    
    # Parse the input data to a numpy array
    input_data = np.array([[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]])
    
    # Perform the predict
    prediction_index = model.predict(input_data)[0]
    
    # Convert predicted index to specie name
    predicted_species = target_names.get(prediction_index, "Unknown")
    
    return {
        "prediction": predicted_species,
        "input data": {
            "sepal length": data.sepal_length,
            "sepal width": data.sepal_width,
            "petal length": data.petal_length,
            "petal width": data.petal_width
        }
    }