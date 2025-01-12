from flask import Flask, jsonify, request
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

app = Flask(__name__)

# Variables globales
PIPELINE = None
ACCURACY = None
F1 = None
INPUT_COLUMNS = None
PORT = 4000

# Función para entrenar el modelo
# Función para entrenar el modelo
def train_model():
    """
    this function trains a model using the heart.csv dataset
    """
    global PIPELINE, ACCURACY, F1, INPUT_COLUMNS

    # Cargar el dataset
    df = pd.read_csv("heart.csv")

    # Separar características y objetivo
    X = df.drop("HeartDisease", axis=1)
    y = df["HeartDisease"]

    # Guardar nombres de las columnas de entrada
    INPUT_COLUMNS = list(X.columns)

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
    PIPELINE = Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("classifier", LogisticRegression(max_iter=10000))
    ])

    # Dividir datos en entrenamiento y prueba
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    # Entrenar el modelo
    PIPELINE.fit(x_train, y_train)

    # Evaluar el modelo
    y_pred = PIPELINE.predict(x_test)
    ACCURACY = accuracy_score(y_test, y_pred)
    F1 = f1_score(y_test, y_pred)


train_model()

@app.route('/metrics', methods=['GET'])
def get_metrics():
    """ 
    this function returns the accuracy and f1 score of the model
    """
    global ACCURACY, F1
    return jsonify({
        "accuracy": ACCURACY,
        "f1_score": F1
    })


@app.route('/predict', methods=['POST'])
def predict():
    """
    this function returns the prediction of the model with data sent in the request
    """
    global PIPELINE, INPUT_COLUMNS

    try:
        # Obtener los datos enviados como JSON
        input_data = request.get_json()

        # Validar que se recibieron las columnas necesarias
        if not all(col in input_data for col in INPUT_COLUMNS):
            return jsonify({"error": "Faltan columnas en los datos enviados"}), 400

        # Crear un DataFrame con los datos recibidos
        input_df = pd.DataFrame([input_data])

        # Hacer la predicción
        prediction = PIPELINE.predict(input_df)

        # Devolver la predicción
        return jsonify({"prediction": int(prediction[0])})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0' ,debug=True, port=PORT)
