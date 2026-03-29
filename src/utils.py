import pandas as pd
import joblib

def load_csv(path):
    return pd.read_csv(path)

def save_csv(df, path):
    df.to_csv(path)

def save_pickle(obj, path):
    joblib.dump(obj, path)

def load_pickle(path):
    return joblib.load(path)