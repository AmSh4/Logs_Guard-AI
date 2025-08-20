
import pandas as pd
import joblib
import re

def extract_features(log_path):
    with open(log_path, 'r') as f:
        log = f.read()
    errors = len(re.findall(r'error|fail|panic', log, re.IGNORECASE))
    cpu_mentions = len(re.findall(r'cpu', log, re.IGNORECASE))
    disk_mentions = len(re.findall(r'disk', log, re.IGNORECASE))
    return pd.DataFrame([[errors, cpu_mentions, disk_mentions]], columns=['errors', 'cpu', 'disk'])

def detect_anomaly(log_path):
    features = extract_features(log_path)
    model = joblib.load('models/anomaly_model.pkl')
    prediction = model.predict(features)[0]
    return 'Anomaly Detected' if prediction == 1 else 'Normal'
