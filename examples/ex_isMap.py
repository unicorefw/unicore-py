# Checks if an object is a dictionary (used as a map in Python).

result = unicore.isMap({"key": "value"})
print(result)  # Output: True

result = unicore.isMap([1, 2, 3])
print(result)  # Output: False