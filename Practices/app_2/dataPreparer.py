from dataFramePreparer import DataFramePreparer
from divideDataset import dataSet, dataSetTrain, dataSetVal

X_df, y_df = dataSet()
X_train, y_train = dataSetTrain()
X_val, y_val = dataSetVal()
data_preparer = DataFramePreparer()

def dataPreparer():
    data_preparer.fit(X_df)
    X_train_prep = data_preparer.transform(X_train)
    X_val_prep = data_preparer.transform(X_val)
    return X_train_prep, X_val_prep, y_train

def dataSetPreparer(dataSet):
    X_prep = data_preparer.transform(dataSet)
    return X_prep
