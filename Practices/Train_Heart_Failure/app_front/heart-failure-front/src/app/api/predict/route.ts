import { NextResponse } from 'next/server'
import {URL} from '../url'

export async function POST(request: Request) {
    const body = await request.json()
    const URL_PREDICT = URL + '/predict'
    if (!URL_PREDICT) {
        return NextResponse.json({ error: 'MODEL_SERVER environment variable is not set' }, { status: 500 });
    }
    const response = await fetch(URL_PREDICT, {
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

