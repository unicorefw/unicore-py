# Counts instances in an array based on a key function's result.

array = ["apple", "banana", "avocado"]
result = unicore.countBy(array, lambda x: x[0])
print(result)  # Output: {"a": 2, "b": 1}