from sklearn.linear_model import LogisticRegression
from dataPreparer import dataPreparer, dataSetPreparer, dataSetVal
from sklearn.metrics import f1_score
from divideDataset import dataSetTest
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

X_test, y_test = dataSetTest()
X_train_prep, X_val_prep, y_train = dataPreparer()
X_val, y_val = dataSetVal()

clf = LogisticRegression(max_iter = 5000)
clf.fit(X_train_prep, y_train)

def f1Score():
    X_test_prep = dataSetPreparer(X_test)
    y_pred = clf.predict(X_test_prep)
    f1Score = f1_score(y_test, y_pred, pos_label = 'anomaly')
    return f1Score

y_pred = clf.predict(X_val_prep)
def precisionScore():
    return precision_score(y_val, y_pred, pos_label = 'anomaly')

def recallScore():
    return recall_score(y_val, y_pred, pos_label = 'anomaly')
