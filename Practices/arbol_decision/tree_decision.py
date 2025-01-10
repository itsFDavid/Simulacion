from sklearn.tree import DecisionTreeClassifier
from scale_dataset import X_test_scale, X_train_scale, X_val_scale
from auxiliar_functions import evaluate_result
from sklearn.metrics import f1_score
from pandas import DataFrame

MAX_DEPTH = 20

X_train_scaled, X_train, y_train = X_train_scale()
X_val_scaled, X_val, y_val = X_val_scale()
X_test_scaled, X_test, y_test = X_test_scale()

X_train_scaled = DataFrame(X_train_scaled, columns=X_train.columns, index=X_train.index)

clf_tree = None
clf_tree_scaled = None


def model_without_scale():
    global clf_tree
    # Modelo entrenado con el conjunto de datos sin escalar
    clf_tree = DecisionTreeClassifier(max_depth=MAX_DEPTH, random_state=42)
    clf_tree.fit(X_train, y_train)
    
def model_with_scale():
    global clf_tree_scaled
    # Modelo entrenado con el conjunto de datos escalado
    clf_tree_scaled = DecisionTreeClassifier(max_depth=MAX_DEPTH, random_state=42)
    clf_tree_scaled.fit(X_train_scaled, y_train)


model_with_scale()
model_without_scale()
def evaluate_model_with_train_set():
    global clf_tree_scaled, clf_tree
    # Predecimos con el conjunto de datos de entrenamiento
    y_train_pred = clf_tree.predict(X_train)
    y_train_prep_pred = clf_tree_scaled.predict(X_train_scaled)
    return evaluate_result(y_train_pred, y_train, y_train_prep_pred, y_train, f1_score)

def evaluate_model_with_val_set():
    global clf_tree_scaled, clf_tree
    # Predecimos con el conjunto de datos de validación
    y_pred = clf_tree.predict(X_val)
    y_prep_pred = clf_tree_scaled.predict(X_val_scaled)
    return evaluate_result(y_pred, y_val, y_prep_pred, y_val, f1_score)