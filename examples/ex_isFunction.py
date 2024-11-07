# Checks if an object is a function.

result = unicore.isFunction(lambda x: x + 1)
print(result)  # Output: True

result = unicore.isFunction(123)
print(result)  # Output: False
