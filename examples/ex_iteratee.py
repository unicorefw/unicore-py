# Returns a function based on value type (identity if callable, otherwise a matcher).

check_name = unicore.iteratee({"name": "Alice"})
print(check_name({"name": "Alice", "age": 25}))  # Output: True

# Using a function as iteratee
double = unicore.iteratee(lambda x: x * 2)
print(double(5))  # Output: 10