from actions.executor import execute_action


# Test 1
result = execute_action(
    action="ALERT_NOW",
    message="Your interview starts in 30 minutes.",
    priority="P0"
)

print("\nResult 1:")
print(result)


# Test 2
result = execute_action(
    action="SHOW_INBOX",
    message="Your package has been shipped.",
    priority="P2"
)

print("\nResult 2:")
print(result)


# Test 3
result = execute_action(
    action="ADD_TO_DIGEST",
    message="Your monthly statement is available.",
    priority="P2"
)

print("\nResult 3:")
print(result)


# Test 4
result = execute_action(
    action="SILENT",
    message="Get 70% off our premium membership!",
    priority="P3"
)

print("\nResult 4:")
print(result)
