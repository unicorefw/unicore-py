# Returns the size of an object (length for lists or dicts, count for generators).

array = [1, 2, 3, 4]
result = unicore.size(array)
print(result)  # Output: 4

obj = {"a": 1, "b": 2}
result = unicore.size(obj)
print(result)  # Output: 2