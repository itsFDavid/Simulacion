import pandas as pd
from train_dataset_split import train_val_test_split


df = pd.read_csv("../../datasetsSVM/Phishing.csv")
train_set, val_set, test_set = train_val_test_split(df)

def divide_train():
    X_train = train_set.drop("URL_Type_obf_Type", axis = 1)
    y_train = train_set["URL_Type_obf_Type"].copy()
    return X_train, y_train


def divide_val():
    X_val = val_set.drop("URL_Type_obf_Type", axis = 1)
    y_val = val_set["URL_Type_obf_Type"].copy()
    return X_val, y_val


def divide_test():
    X_test = test_set.drop("URL_Type_obf_Type", axis = 1)
    y_test = test_set["URL_Type_obf_Type"].copy()
    return X_test, y_test