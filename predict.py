

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib

 
def load_model():
    # Modeli ve scaler'ı yükleyin
    model = joblib.load('random_forest_model.joblib')
    scaler = StandartScaler
    return model, scaler

def predict_obesity(model, scaler, user_data):
    # Verileri ölçeklendirin
    user_data_scaled = scaler.transform(user_data)

    # Tahmini yapın
    prediction = model.predict(user_data_scaled)
    prediction_proba = model.predict_proba(user_data_scaled)
    
    return prediction, prediction_proba