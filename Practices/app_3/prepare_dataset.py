import pandas as pd
from sklearn.impute import SimpleImputer
from dataset_divide import divide_test, divide_train, divide_val


X_train_, y_train = divide_train()
X_val_, y_val = divide_val()
X_test_, y_test = divide_test()


def prepare_dataset():
    """Preparar el conjunto de datos para el entrenamiento del modelo"""
    # Eliminar los atributos que contengan valores infinitos
    X_train = X_train_.drop("argPathRatio", axis = 1)
    X_val = X_val_.drop("argPathRatio", axis = 1)
    X_test = X_test_.drop("argPathRatio", axis = 1)
    # Rellenar los valores nulos con la mediana

    imputer = SimpleImputer(strategy="median")
    X_train_prep = imputer.fit_transform(X_train)
    X_val_prep = imputer.fit_transform(X_val)
    X_test_prep = imputer.fit_transform(X_test)
    # Transformar el DataFrame de Pandas
    X_train_prep = pd.DataFrame(X_train_prep, columns = X_train.columns, index = X_train.index)
    X_val_prep = pd.DataFrame(X_val_prep, columns = X_val.columns, index = X_val.index)
    X_test_prep = pd.DataFrame(X_test_prep, columns = X_test.columns, index = X_test.index)
    return X_train_prep, X_val_prep, X_test_prep
