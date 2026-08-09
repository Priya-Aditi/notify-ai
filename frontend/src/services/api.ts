import type {
  MessagesResponse,
  AnalysisResult
} from "../types/message";


const API_BASE_URL = "http://localhost:8000";


export async function getMessages(): Promise<MessagesResponse> {

  const response = await fetch(
    `${API_BASE_URL}/messages`
  );

  if (!response.ok) {
    throw new Error("Failed to fetch messages");
  }

  return response.json();
}

export async function analyzeMessage(
  message: string
): Promise<AnalysisResult> {

  const response = await fetch(
    `${API_BASE_URL}/analyze`,
    {
      method: "POST",

      headers: {
        "Content-Type": "application/json",
      },

      body: JSON.stringify({
        message,
      }),
    }
  );


  if (!response.ok) {
    throw new Error("Failed to analyze message");
  }


  return response.json();
}