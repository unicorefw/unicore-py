# Checks if an object is a WeakKeyDictionary.
 
from weakref import WeakKeyDictionary
result = unicore.isWeakMap(WeakKeyDictionary())
print(result)  # Output: True

result = unicore.isWeakMap({})
print(result)  # Output: False