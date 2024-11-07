# Generates a unique ID, optionally prefixed.

result = unicore.uniqueId("user_")
print(result)  # Output: "user_1" (ID will increment with each call)

result = unicore.uniqueId("order_")
print(result)  # Output: "order_2"