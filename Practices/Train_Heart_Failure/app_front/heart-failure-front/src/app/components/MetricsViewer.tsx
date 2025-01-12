"use client";

import { useState, useEffect } from "react";

interface Metrics {
  accuracy: number;
  f1_score: number;
}

export default function MetricsViewer() {
  const [metrics, setMetrics] = useState<Metrics | null>(null);

  useEffect(() => {
    fetch("/api/metrics")
      .then((response) => response.json())
      .then((data) => setMetrics(data))
      .catch((error) => console.error("Error fetching metrics:", error));
  }, []);

  return (
    <div className="bg-black shadow-md rounded px-4 sm:px-6 lg:px-8 pt-4 sm:pt-6 lg:pt-8 pb-4 sm:pb-6 lg:pb-8 mb-4">
      <h2 className="text-lg sm:text-xl lg:text-2xl font-bold mb-4">
        Métricas del Modelo
      </h2>
      {metrics ? (
        <div>
          <p className="text-sm sm:text-base lg:text-lg mb-2">
            Precisión: {(metrics.accuracy * 100).toFixed(2)}%
          </p>
          <p className="text-sm sm:text-base lg:text-lg">
            F1 Score: {(metrics.f1_score * 100).toFixed(2)}%
          </p>
        </div>
      ) : (
        <p>Loading metrics...</p>
      )}
    </div>
  );
}
