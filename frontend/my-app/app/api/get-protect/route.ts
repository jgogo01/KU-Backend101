import { NextResponse } from "next/server";

export async function GET() {
  try {
    const response = await fetch(`${process.env.API_URL}/protected`, {
      method: "POST",
      headers: {
        "X-API-KEY": process.env.API_KEY || "",
      },
    });

    const data = await response.json();
    return NextResponse.json(data);
  } catch (error) {
    console.error("Error in get-protect API:", error);
    return NextResponse.json({ error: "Failed to fetch protected data" }, { status: 500 });
  }
}
