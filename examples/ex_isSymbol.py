# Checks if an object is a unique constant-like object (None, NotImplemented, Ellipsis).

result = unicore.isSymbol(None)
print(result)  # Output: True

result = unicore.isSymbol("hello")
print(result)  # Output: False