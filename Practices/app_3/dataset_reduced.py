import pandas as pd

from prepare_dataset import prepare_dataset

X_train_prep, X_val_prep, X_test_prep = prepare_dataset()

def reduce_dataset():
    # Reducir el DataSet para representarlo graficamente
    X_train_reduced = X_train_prep[["domainUrlRatio", "domainlength"].copy()]
    X_val_reduced = X_val_prep[["domainUrlRatio", "domainlength"].copy()]
    return X_train_reduced, X_val_reduced