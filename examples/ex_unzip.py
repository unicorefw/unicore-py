# Splits tuples back into separate arrays.

array_of_tuples = [(1, "a"), (2, "b"), (3, "c")]
result = unicore.unzip(array_of_tuples)
print(result)  # Output: [[1, 2, 3], ["a", "b", "c"]]

