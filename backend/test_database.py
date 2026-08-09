from database.db import initialize_database, save_message, get_messages


initialize_database()

message_id = save_message(
    message="Please send the project report by 4 PM.",
    summary="Request for project report",
    category="work",
    importance=8,
    urgency=9,
    requires_action=True,
    deadline="4 PM today",
    suggested_action="Send the project report",
    priority="P0",
    priority_label="Critical",
    priority_score=10.8,
    notification_action="ALERT_NOW",
    notification_reason="Critical message requires immediate attention."
)

print("Saved message ID:", message_id)

messages = get_messages()

print("\nMessages in database:")

for message in messages:
    print(message)
