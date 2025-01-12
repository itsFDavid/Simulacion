import { NextResponse } from 'next/server'

export async function POST(request: Request) {
    const body = await request.json()
    const URL = "http://127.0.0.1:4000/predict"
    const response = await fetch(URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(body),
    });

    if (!response.ok) {
        return NextResponse.json({ error: 'Failed to make prediction' }, { status: 500 });
    }

    const prediction = await response.json()
  return NextResponse.json({ prediction })
}

