# Sorts an array based on a function applied to each element.

array = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 20}]
result = unicore.sortBy(array, lambda x: x["age"])
print(result)  # Output: [{"name": "Bob", "age": 20}, {"name": "Alice", "age": 25}]
