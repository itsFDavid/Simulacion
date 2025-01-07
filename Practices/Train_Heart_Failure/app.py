from flask import Flask, jsonify
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

# Inicializar Flask
app = Flask(__name__)

# Variables globales para almacenar el modelo y métricas
pipeline = None
accuracy = None
f1 = None

# Función para entrenar el modelo
def train_model():
    global pipeline, accuracy, f1

    # Cargar el dataset
    df = pd.read_csv("heart.csv")  # Asegúrate de que el archivo esté en el mismo directorio

    # Separar características y objetivo
    X = df.drop("HeartDisease", axis=1)
    y = df["HeartDisease"]

    # Identificar columnas categóricas y numéricas
    categorical_columns = X.select_dtypes(include="object").columns
    numeric_columns = X.select_dtypes(exclude="object").columns

    # Crear preprocesamiento
    categorical_preprocessor = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ])

    numeric_preprocessor = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="mean")),
        ("scaler", StandardScaler())
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_preprocessor, numeric_columns),
            ("cat", categorical_preprocessor, categorical_columns)
        ]
    )

    # Crear pipeline
    pipeline = Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("classifier", LogisticRegression(max_iter=10000))
    ])

    # Dividir datos en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    # Entrenar el modelo
    pipeline.fit(X_train, y_train)

    # Evaluar el modelo
    y_pred = pipeline.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

# Entrenar el modelo al iniciar el servidor
train_model()

@app.route('/metrics', methods=['GET'])
def get_metrics():
    global accuracy, f1
    # Devolver las métricas en formato JSON
    return jsonify({
        "accuracy": accuracy,
        "f1_score": f1
    })

if __name__ == '__main__':
    app.run(debug=True)
