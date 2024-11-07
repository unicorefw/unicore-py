# Checks if an object is a DataView equivalent (memoryview in Python).

buffer = bytearray([1, 2, 3])
view = memoryview(buffer)
result = unicore.isDataView(view)
print(result)  # Output: True

result = unicore.isDataView(buffer)
print(result)  # Output: False