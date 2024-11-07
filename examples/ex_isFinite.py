# Checks if a number is finite (not infinite or NaN).
 
result = unicore.isFinite(123)
print(result)  # Output: True

result = unicore.isFinite(float('inf'))
print(result)  # Output: False