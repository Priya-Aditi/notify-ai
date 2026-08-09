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

export interface AnalysisResult {
  message_id: number;

  analysis: {
    summary: string;
    category: string;
    importance: number;
    urgency: number;
    requires_action: boolean;
    deadline: string | null;
    suggested_action: string | null;
  };

  priority: {
    priority: string;
    label: string;
    score: number;
    reason: string;
  };

  notification: {
    action: string;
    reason: string;
  };

  action: {
    executed: boolean;
    action: string;
    message: string;
  };
}