# Checks if an object is an ArrayBuffer equivalent (bytearray or memoryview in Python).
 
result = unicore.isArrayBuffer(bytearray([1, 2, 3]))
print(result)  # Output: True

result = unicore.isArrayBuffer("hello")
print(result)  # Output: False