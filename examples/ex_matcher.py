# Returns a function that checks if an object matches key-value pairs.
 
check = unicore.matcher({"name": "Alice"})
print(check({"name": "Alice", "age": 25}))  # Output: True