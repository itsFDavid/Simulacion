"use client";

import { useState, useEffect } from "react";
import MetricsViewer from "./components/MetricsViewer";
import PredictionForm from "./components/PredictionForm";

export default function Home() {
  const [testData, setTestData] = useState([]);

  useEffect(() => {
    fetch("/api/test-data")
      .then((response) => response.json())
      .then((data) => setTestData(data))
      .catch((error) => console.error("Error fetching test data:", error));
  }, []);

  return (
    <main className="container mx-auto p-4">
      <h1 className="text-3xl font-bold mb-6">
        Detector de enfermedad al corazón
      </h1>
      {/* Contenedor principal en forma de grid */}
      <div className="grid grid-cols-1 lg:grid-cols-1 gap-6">
        {/* Primer componente: MetricsViewer */}
        <div className="w-full">
          <MetricsViewer />
        </div>

        {/* Segundo componente: PredictionForm */}
        <div className="w-full">
          <PredictionForm testData={testData} />
        </div>
      </div>
    </main>
  );
}
