import { NextResponse } from 'next/server';
import fs from 'fs';
import path from 'path';

export async function GET() {
    // Ruta relativa a la raíz del proyecto, dentro de 'public'
    const filePath = path.resolve('public/tests.json');

    try {
        // Lee el contenido del archivo
        const fileContents = fs.readFileSync(filePath, 'utf8');
        const testData = JSON.parse(fileContents);
        return NextResponse.json(testData);
    } catch (error) {
        console.error('Error reading test data:', error);
        return NextResponse.json({ error: 'Error reading test data' }, { status: 500 });
    }
}
