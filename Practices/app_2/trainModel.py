from sklearn.linear_model import LogisticRegression
from dataPreparer import dataPreparer, dataSetPreparer
from sklearn.metrics import f1_score
from divideDataset import dataSetTest

X_test, y_test = dataSetTest()

X_train_prep, X_val_prep, y_train = dataPreparer()

clf = LogisticRegression(max_iter = 5000)
clf.fit(X_train_prep, y_train)

def predict():
    X_test_prep = dataSetPreparer(X_test)
    y_pred = clf.predict(X_test_prep)
    f1Score = f1_score(y_test, y_pred, pos_label = 'anomaly')
    return f1Score
