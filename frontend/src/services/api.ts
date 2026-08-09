import type { MessagesResponse } from "../types/message";


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