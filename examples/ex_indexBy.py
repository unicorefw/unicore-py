# Indexes an array by a function’s result for each element.

array = [{"name": "Alice"}, {"name": "Bob"}]
result = unicore.indexBy(array, lambda x: x["name"])
print(result)  # Output: {"Alice": {"name": "Alice"}, "Bob": {"name": "Bob"}}