"use client";

import { useState } from "react";

export default function TestDataSelector({ testData, onSelectData }) {
  const [selectedData, setSelectedData] = useState(null);

  const handleSelect = (data) => {
    setSelectedData(data);
    console.log("Selected data:", data);
    // Llamamos a la función pasada como prop para actualizar los datos en el formulario
    onSelectData(data);
  };

  return (
    <div>
      <div className="bg-black shadow-md rounded px-4 sm:px-6 lg:px-8 pt-4 sm:pt-6 lg:pt-8 pb-4 sm:pb-6 lg:pb-8 mb-4 w-full">
        <h2 className="text-lg sm:text-xl lg:text-2xl font-bold mb-4">
          Datos de Prueba
        </h2>
        <div className="h-[300px] sm:h-[500px] lg:h-[620px] overflow-y-auto">
          {testData.map((data, index) => (
            <div
              key={index}
              className="cursor-pointer hover:bg-gray-500 p-2 rounded"
              onClick={() => handleSelect(data)}
            >
              <p className="text-sm sm:text-base lg:text-lg">
                Edad: {data.Age}, Sexo: {data.Sex}, Tipo de Dolor en Pecho:{" "}
                {data.ChestPainType}, Enfermo del corazón:{" "}
                {data.HeartDisease ? "Sí" : "No"}
              </p>
            </div>
          ))}
        </div>
      </div>

      {selectedData && (
        <div className="mt-4">
          <h3 className="text-xl font-bold mb-2 ">Selected Data</h3>
          <pre className="bg-gray-600 p-2 rounded">
            {JSON.stringify(selectedData, null, 2)}
          </pre>
        </div>
      )}
    </div>
  );
}
