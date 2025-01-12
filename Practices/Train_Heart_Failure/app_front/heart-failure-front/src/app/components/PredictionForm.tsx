"use client";

import { useState } from "react";
import TestDataSelector from "./TestDataSelector"; // Asegúrate de importar el componente
import { TestData } from "../common/test-data.interface";

interface PredictionFormProps {
  testData: TestData[];
}

export default function PredictionForm({ testData }: PredictionFormProps) {
  const [formData, setFormData] = useState({
    Age: "",
    Sex: "",
    ChestPainType: "",
    RestingBP: "",
    Cholesterol: "",
    FastingBS: "",
    RestingECG: "",
    MaxHR: "",
    ExerciseAngina: "",
    Oldpeak: "",
    ST_Slope: "",
    HeartDisease: "",
  });
  const [prediction, setPrediction] = useState<number | null>(null);

  // Mapeo de keys en inglés a etiquetas en español
  const translations = {
    Age: "Edad",
    Sex: "Sexo",
    ChestPainType: "Tipo de Dolor en el Pecho",
    RestingBP: "Presión Arterial en Reposo",
    Cholesterol: "Colesterol",
    FastingBS: "Azúcar en Ayunas",
    RestingECG: "ECG en Reposo",
    MaxHR: "Frecuencia Cardíaca Máxima",
    ExerciseAngina: "Angina por Ejercicio",
    Oldpeak: "Desnivel del ST",
    ST_Slope: "Pendiente del ST",
    HeartDisease: "Enfermedad del Corazón",
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  interface PredictionResponse {
    prediction: {
      prediction: number;
    };
  }

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    fetch("/api/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    })
      .then((response) => response.json())
      .then((data: PredictionResponse) => {
        setPrediction(data.prediction.prediction);
      })
      .catch((error) =>
        console.error("Error al realizar la predicción:", error)
      );
  };

  const handleSelectData = (data: TestData) => {
    setFormData({
      Age: data.Age.toString(),
      Sex: data.Sex,
      ChestPainType: data.ChestPainType,
      RestingBP: data.RestingBP.toString(),
      Cholesterol: data.Cholesterol.toString(),
      FastingBS: data.FastingBS.toString(),
      RestingECG: data.RestingECG,
      MaxHR: data.MaxHR.toString(),
      ExerciseAngina: data.ExerciseAngina,
      Oldpeak: data.Oldpeak.toString(),
      ST_Slope: data.ST_Slope,
      HeartDisease: data.HeartDisease.toString(),
    });
  };

  return (
    <div className="w-full flex flex-col lg:flex-row space-y-6 lg:space-y-0 lg:space-x-6">
      {/* Columna izquierda */}
      <div className="w-full lg:w-1/2 h-auto lg:h-[500px] bg-black shadow-md rounded px-4 sm:px-6 lg:px-8 pt-4 sm:pt-6 lg:pt-8 pb-4 sm:pb-6 lg:pb-8">
        <TestDataSelector testData={testData} onSelectData={handleSelectData} />
      </div>

      {/* Columna derecha */}
      <div className="w-full lg:w-1/2 bg-gray-400 shadow-md rounded px-4 sm:px-6 lg:px-8 pt-4 sm:pt-6 lg:pt-8 pb-4 sm:pb-6 lg:pb-8">
        <h2 className="text-lg sm:text-xl lg:text-2xl font-bold mb-4">
          Formulario de Predicción
        </h2>
        <form onSubmit={handleSubmit}>
          {Object.keys(formData).map((key) => (
            <div key={key} className="mb-4">
              <label
                className="block text-gray-700 text-sm sm:text-base font-bold mb-2"
                htmlFor={key}
              >
                {translations[key as keyof typeof formData]}
              </label>
              <input
                className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                id={key}
                name={key}
                type="text"
                value={formData[key as keyof typeof formData]}
                onChange={handleChange}
              />
            </div>
          ))}

          <button
            className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
            type="submit"
          >
            Predecir
          </button>
        </form>
        {prediction !== null && (
          <div
            className={`mt-4 p-4 rounded ${
              prediction === 1
                ? "bg-red-100 text-red-700"
                : "bg-green-100 text-green-700"
            }`}
          >
            {prediction === 1
              ? "Se detectó enfermedad cardíaca 🚨"
              : "No se detectó enfermedad cardíaca 🎉"}
          </div>
        )}
      </div>
    </div>
  );
}
