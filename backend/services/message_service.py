from ai.analyzer import analyze_message
from priority.engine import calculate_priority
from notification.engine import decide_notification
from actions.executor import execute_action
from database.db import save_message


def process_message(message: str):

    # Step 1: Understand the message
    analysis = analyze_message(message)

    # Step 2: Calculate priority
    priority = calculate_priority(analysis)

    # Step 3: Decide notification behavior
    notification = decide_notification(
        priority=priority["priority"],
        category=analysis.category,
        requires_action=analysis.requires_action
    )

    # Step 4: Save the message
    message_id = save_message(
        message=message,
        summary=analysis.summary,
        category=analysis.category,
        importance=analysis.importance,
        urgency=analysis.urgency,
        requires_action=analysis.requires_action,
        deadline=analysis.deadline,
        suggested_action=analysis.suggested_action,
        priority=priority["priority"],
        priority_label=priority["label"],
        priority_score=priority["score"],
        notification_action=notification["action"],
        notification_reason=notification["reason"]
    )

    # Step 5: Execute notification decision
    action_result = execute_action(
        action=notification["action"],
        message=message,
        priority=priority["priority"]
    )

    # Step 6: Return complete result
    return {
        "message_id": message_id,
        "analysis": analysis,
        "priority": priority,
        "notification": notification,
        "action": action_result
    }
