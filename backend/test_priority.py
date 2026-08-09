from ai.schemas import MessageAnalysis
from priority.engine import calculate_priority


analysis = MessageAnalysis(
    summary="Recruiter requested interview availability",
    category="career",
    importance=8,
    urgency=7,
    requires_action=True,
    deadline=None,
    suggested_action="Reply with interview availability"
)


result = calculate_priority(analysis)

print(result)
