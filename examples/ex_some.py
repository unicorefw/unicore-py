# Checks if at least one element in the array matches the predicate.

array = [1, 2, 3, 4]
result = unicore.some(array, lambda x: x > 2)
print(result)  # Output: True