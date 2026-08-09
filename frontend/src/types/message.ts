export interface Message {
  id: number;
  message: string;
  summary: string | null;
  category: string | null;
  importance: number | null;
  urgency: number | null;
  requires_action: boolean;
  deadline: string | null;
  suggested_action: string | null;
  priority: string | null;
  priority_label: string | null;
  priority_score: number | null;
  notification_action: string | null;
  notification_reason: string | null;
  is_read: boolean;
  created_at: string;
}

export interface MessagesResponse {
  messages: Message[];
}