# Checks if an object is a regular expression.

import re
result = unicore.isRegExp(re.compile(r"\d+"))
print(result)  # Output: True

result = unicore.isRegExp("hello")
print(result)  # Output: False