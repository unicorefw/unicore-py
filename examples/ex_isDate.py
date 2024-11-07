# Checks if an object is a date.
 
from datetime import date
result = unicore.isDate(date.today())
print(result)  # Output: True

result = unicore.isDate("2023-01-01")
print(result)  # Output: False