import { NextResponse } from 'next/server'

export async function GET() {
  const URL = "http://127.0.0.1:4000/metrics"
  const response = await fetch(URL)

  if (!response.ok) {
    return NextResponse.json({ error: 'Failed to fetch metrics' }, { status: 500 });
  }

  // Leer el cuerpo de la respuesta como JSON
  const metrics = await response.json()
  return NextResponse.json(metrics)
}
