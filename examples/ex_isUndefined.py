# Checks if an object is None (since Python doesn’t have undefined).

result = unicore.isUndefined(None)
print(result)  # Output: True

result = unicore.isUndefined(123)
print(result)  # Output: False