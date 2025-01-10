import pandas as pd

def load_dataset():
    df = pd.read_csv('../../datasets/TotalFeatures-ISCXFlowMeter.csv')
    return df
