
# Usage
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from unicore import unicore  # Now you can import unicore as usual


# Wraps an object in a chainable class, allowing method chaining.

result = unicore.chain([1, 2, 3, 4]) \
                 .map(lambda x: x * 2) \
                 .filter(lambda x: x > 4) \
                 .value()
print(result)  # Output: [6, 8]


# Example 1: Using chain with a string
result = unicore.chain("hello")\
    .map(lambda c: c.upper())\
    .reverse()\
    .value()

print(result)  # Output: "OLLEH"

# Example 2: Sorting a string
result = unicore.chain("banana")\
    .sortBy()\
    .value()

print(result)  # Output: "aaabnn"

# Example 3: Getting the first character(s) of a string
result = unicore.chain("world")\
    .first(3)\
    .value()

print(result)  # Output: "wor"

# Example 4: Combining methods
result = unicore.chain("apple")\
    .map(lambda c: c.upper())\
    .sortBy()\
    .first(3)\
    .value()

print(result)  # Output: "AEL"

# Example 5: Original list remains unchanged
original_list = [3, 1, 4, 1, 5]
result = unicore.chain(original_list)\
    .sortBy()\
    .reverse()\
    .value()

print(result)         # Output: [5, 4, 3, 1, 1]
print(original_list)  # Output: [3, 1, 4, 1, 5]