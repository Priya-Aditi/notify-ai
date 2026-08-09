from ai.schemas import MessageAnalysis


def calculate_priority(analysis: MessageAnalysis) -> dict:

    # --------------------------------------------------
    # Rule 1: Promotional messages are low priority
    # --------------------------------------------------

    if analysis.category.lower() == "promotion":
        return {
            "priority": "P3",
            "label": "Low",
            "score": 0,
            "reason": "Promotional messages are treated as low priority."
        }

    # --------------------------------------------------
    # Calculate base score
    # --------------------------------------------------

    score = (
        analysis.importance * 0.4
        + analysis.urgency * 0.4
    )

    # --------------------------------------------------
    # Rule 2: Action required
    # --------------------------------------------------

    if analysis.requires_action:
        score += 2

    # --------------------------------------------------
    # Rule 3: Deadline exists
    # --------------------------------------------------

    if analysis.deadline:
        score += 2

    # --------------------------------------------------
    # Determine priority
    # --------------------------------------------------

    if score >= 9:
        priority = "P0"
        label = "Critical"

    elif score >= 7:
        priority = "P1"
        label = "High"

    elif score >= 4:
        priority = "P2"
        label = "Normal"

    else:
        priority = "P3"
        label = "Low"

    # --------------------------------------------------
    # Create explanation
    # --------------------------------------------------

    reasons = []

    if analysis.importance >= 7:
        reasons.append("high importance")

    if analysis.urgency >= 7:
        reasons.append("high urgency")

    if analysis.requires_action:
        reasons.append("action required")

    if analysis.deadline:
        reasons.append("deadline present")

    if not reasons:
        reasons.append("low importance and urgency")

    reason = ", ".join(reasons)

    return {
        "priority": priority,
        "label": label,
        "score": round(score, 2),
        "reason": reason
    }
