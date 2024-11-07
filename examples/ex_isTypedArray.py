# Checks if an object is an array.array type.
 
from array import array
result = unicore.isTypedArray(array('i', [1, 2, 3]))
print(result)  # Output: True

result = unicore.isTypedArray([1, 2, 3])
print(result)  # Output: False