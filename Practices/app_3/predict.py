from sklearn.svm import SVC
from sklearn.metrics import f1_score
from sklearn.preprocessing import StandardScaler, RobustScaler
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.datasets import make_moons
from sklearn.svm import LinearSVC
from sklearn.preprocessing import PolynomialFeatures
from dataset_reduced import reduce_dataset
from dataset_divide import divide_train, divide_val, divide_test
from prepare_dataset import prepare_dataset

X_train, y_train = divide_train()
X_val, y_val = divide_val()
X_test, y_test = divide_test()

X_train_reduced, X_val_reduced = reduce_dataset()
X_train_prep, X_val_prep, X_test_prep = prepare_dataset()

y_train_num = y_train.factorize()[0]
y_val_num = y_val.factorize()[0]

svm_clf = SVC(kernel = "linear", C=1)
svm_clf.fit(X_train_prep, y_train)

svm_clf_sc = Pipeline([
    ("scaler", RobustScaler()),
    ("linear_svc", SVC(kernel= "linear", C=50))
    ])
svm_clf_sc.fit(X_train_reduced, y_train)

polynomial_svm_clf = Pipeline([
    ("poly_features", PolynomialFeatures(degree=3)),
    ("scaler", StandardScaler()),
    ("svm_clf", LinearSVC(C = 20, loss = "hinge", random_state = 42, max_iter = 100000))
])
polynomial_svm_clf.fit(X_train_reduced, y_train_num)

def model_reduced_predict():
    """Predict the reduced dataset"""
    y_pred = svm_clf_sc.predict(X_val_reduced)
    return y_pred


def get_f1_score_reduced():
    """Get the f1 score of the reduced dataset"""
    y_pred = model_reduced_predict()
    return f1_score(y_pred, y_val, pos_label = 'phishing')


def model_predict():
    """Predict the dataset"""
    y_pred = svm_clf.predict(X_val_prep)
    return y_pred

def get_f1_score():
    """Get the f1 score of the dataset"""
    y_pred = model_predict()
    return f1_score(y_pred, y_val, pos_label = 'phishing')

def model_polynomial():
    """Predict the polynomial dataset"""
    y_pred = polynomial_svm_clf.predict(X_val_reduced)
    return y_pred

def get_f1_score_polynomial():
    """Get the f1 score of the polynomial dataset"""
    y_pred = model_polynomial()
    return f1_score(y_pred, y_val_num)
