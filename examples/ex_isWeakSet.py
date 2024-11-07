# Checks if an object is a WeakSet.

from weakref import WeakSet
result = unicore.isWeakSet(WeakSet())
print(result)  # Output: True

result = unicore.isWeakSet({1, 2, 3})
print(result)  # Output: False