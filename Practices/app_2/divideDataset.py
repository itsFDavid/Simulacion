from split_test import train_val_test_split
from load_kdd import load_kdd_dataset
import pandas as pd

df = load_kdd_dataset("../../datasets/NSL-KDD/KDDTrain+.arff")
train_set, val_set, test_set = train_val_test_split(df)

def dataSet():
    # DataSet General
    X_df = df.drop("class", axis = 1)
    y_df = df["class"].copy()
    return X_df, y_df

def dataSetTest():
    # DataSet de test
    X_test = test_set.drop("class", axis = 1)
    y_test = test_set["class"].copy()
    return X_test, y_test

def dataSetVal():
    # DataSet de Validacion
    X_val = val_set.drop("class", axis = 1)
    y_val = val_set["class"].copy()
    return X_val, y_val
def dataSetTrain():
    # DataSet de entrenamiento
    X_train = train_set.drop("class", axis = 1)
    y_train = train_set["class"].copy()
    return X_train, y_train
