import { NextResponse } from 'next/server'
import {URL} from '../url'

export async function GET() {
  const URL_METRICS = URL + '/metrics'
  if (!URL_METRICS) {
    return NextResponse.json({ error: 'MODEL_SERVER environment variable is not set' }, { status: 500 });
  }
  const response = await fetch(URL_METRICS)

  if (!response.ok) {
    return NextResponse.json({ error: 'Failed to fetch metrics' }, { status: 500 });
  }

  // Leer el cuerpo de la respuesta como JSON
  const metrics = await response.json()
  return NextResponse.json(metrics)
}
