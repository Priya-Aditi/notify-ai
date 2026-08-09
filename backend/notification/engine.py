from typing import Literal


NotificationAction = Literal[
    "ALERT_NOW",
    "SHOW_INBOX",
    "ADD_TO_DIGEST",
    "SILENT"
]


def decide_notification(
    priority: str,
    category: str,
    requires_action: bool
) -> dict:

    category = category.lower()

    # --------------------------------------------
    # Rule 1: Promotional messages
    # --------------------------------------------

    if category == "promotion":
        return {
            "action": "SILENT",
            "reason": "Promotional messages should not interrupt the user."
        }

    # --------------------------------------------
    # Rule 2: Critical messages
    # --------------------------------------------

    if priority == "P0":
        return {
            "action": "ALERT_NOW",
            "reason": "Critical message requires immediate attention."
        }

    # --------------------------------------------
    # Rule 3: High priority messages
    # --------------------------------------------

    if priority == "P1":
        if requires_action:
            return {
                "action": "ALERT_NOW",
                "reason": "High-priority message requires user action."
            }

        return {
            "action": "SHOW_INBOX",
            "reason": "High-priority message should be visible to the user."
        }

    # --------------------------------------------
    # Rule 4: Normal messages
    # --------------------------------------------

    if priority == "P2":

        if requires_action:
            return {
                "action": "SHOW_INBOX",
                "reason": "Normal-priority message requires user action."
            }

        return {
            "action": "ADD_TO_DIGEST",
            "reason": "Normal message can be grouped into a later digest."
        }

    # --------------------------------------------
    # Rule 5: Low priority
    # --------------------------------------------

    return {
        "action": "SILENT",
        "reason": "Low-priority message does not require immediate attention."
    }
