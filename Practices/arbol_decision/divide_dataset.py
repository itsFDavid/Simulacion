from load_dataset import load_dataset
from auxiliar_functions import remove_labels, train_val_test_split

df = load_dataset()

# Copiamos el conjunto de datos y
# transformamos la variable de salida a numérica para calcular correlaciones
X = df.copy()
X['calss'] = X['calss'].factorize()[0]

# Calculamos correlaciones
corr_matrix = X.corr()
corr_matrix["calss"].sort_values(ascending=False)
X.corr()


# Dividimos el conjunto de datos
train_seta, val_seta, test_seta = train_val_test_split(X)

def train_set():
    X_train, y_train = remove_labels(train_seta, 'calss')
    return X_train, y_train

def val_set():
    X_val, y_val = remove_labels(val_seta, 'calss')
    return X_val, y_val

def test_set():
    X_test, y_test = remove_labels(test_seta, 'calss')
    return X_test, y_test