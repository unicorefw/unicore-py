# Checks if an object has a specified property.

obj = {"name": "Alice", "age": 25}
result = unicore.has(obj, "age")
print(result)  # Output: True

result = unicore.has(obj, "city")
print(result)  # Output: False