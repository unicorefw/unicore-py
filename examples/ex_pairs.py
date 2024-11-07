# Converts an object’s properties into an array of [key, value] pairs.

obj = {"name": "Alice", "age": 25}
result = unicore.pairs(obj)
print(result)  # Output: [("name", "Alice"), ("age", 25)]