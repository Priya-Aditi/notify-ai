from notification.engine import decide_notification


# Test 1: Critical work message
result = decide_notification(
    priority="P0",
    category="work",
    requires_action=True
)

print("Test 1:")
print(result)


# Test 2: Promotion
result = decide_notification(
    priority="P3",
    category="promotion",
    requires_action=False
)

print("\nTest 2:")
print(result)


# Test 3: Normal shopping update
result = decide_notification(
    priority="P2",
    category="shopping",
    requires_action=False
)

print("\nTest 3:")
print(result)


# Test 4: High-priority career message
result = decide_notification(
    priority="P1",
    category="career",
    requires_action=True
)

print("\nTest 4:")
print(result)

result = decide_notification(
    priority="P1",
    category="career",
    requires_action=False
)

print("\nTest 5:")
print(result)
