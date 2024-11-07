# Checks if an object is a tuple, which is the closest to the concept of arguments in Python.
 
result = unicore.isArguments((1, 2, 3))
print(result)  # Output: True

result = unicore.isArguments([1, 2, 3])
print(result)  # Output: False