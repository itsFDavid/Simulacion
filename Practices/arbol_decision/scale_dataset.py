from divide_dataset import test_set, val_set, train_set
from sklearn.preprocessing import RobustScaler
from pandas import DataFrame

X_train, y_train = train_set()
X_val, y_val = val_set()
X_test, y_test = test_set()


def X_train_scale():
    scaler = RobustScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    return X_train_scaled, X_train, y_train


def X_test_scale():
    scaler = RobustScaler()
    X_test_scaled = scaler.fit_transform(X_test)
    return X_test_scaled, X_test, y_test


def X_val_scale():
    scaler = RobustScaler()
    X_test_scaled = scaler.fit_transform(X_test)
    return X_test_scaled, X_val, y_val
