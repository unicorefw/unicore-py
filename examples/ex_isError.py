# Checks if an object is an exception.

result = unicore.isError(ValueError("An error occurred"))
print(result)  # Output: True

result = unicore.isError("error")
print(result)  # Output: False