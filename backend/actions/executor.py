def execute_action(
    action: str,
    message: str,
    priority: str
) -> dict:

    if action == "ALERT_NOW":
        return send_alert(message, priority)

    elif action == "SHOW_INBOX":
        return add_to_inbox(message, priority)

    elif action == "ADD_TO_DIGEST":
        add_to_digest(message, priority)

        return {
            "executed": True,
            "action": "ADD_TO_DIGEST",
            "message": "Message added to digest."
        }

    elif action == "SILENT":
        return {
            "executed": True,
            "action": "SILENT",
            "message": "No notification sent."
        }

    return {
        "executed": False,
        "action": action,
        "message": "Unknown notification action."
    }


def send_alert(message: str, priority: str) -> dict:

    print("\n🔔 ALERT NOW")
    print(f"Priority: {priority}")
    print(f"Message: {message}")

    return {
        "executed": True,
        "action": "ALERT_NOW",
        "message": "Alert triggered."
    }


def add_to_inbox(message: str, priority: str) -> dict:

    print("\n📥 ADD TO INBOX")
    print(f"Priority: {priority}")
    print(f"Message: {message}")

    return {
        "executed": True,
        "action": "SHOW_INBOX",
        "message": "Message added to inbox."
    }


def add_to_digest(message: str, priority: str):

    print("\n📋 ADD TO DIGEST")
    print(f"Priority: {priority}")
    print(f"Message: {message}")
