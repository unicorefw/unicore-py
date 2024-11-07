# Checks if an object has matching key-value pairs.

obj = {"name": "Alice", "age": 25}
result = unicore.isMatch(obj, {"name": "Alice"})
print(result)  # Output: True

result = unicore.isMatch(obj, {"name": "Bob"})
print(result)  # Output: False