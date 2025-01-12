import requests
import pandas as pd

# URL de la API
url = "http://127.0.0.1:4000/predict"

# Leer los datos de prueba desde el archivo JSON
data = pd.read_json("tests.json")

# Iterar sobre cada fila del DataFrame
for _, row in data.iterrows():
    # Convertir la fila a un diccionario
    entry = row.to_dict()
    true_value = entry.get("HeartDisease")  # Obtener el valor original de HeartDisease
    try:
        # Enviar la solicitud POST con la fila convertida
        response = requests.post(url, json=entry)
        if response.status_code == 200:
            prediction = response.json()  # Obtener la predicción del servidor
            print(f"True Value: {true_value}, Predicted Value: {prediction}")
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Failed to send data: {e}")
