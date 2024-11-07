
# Usage
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from unicore import unicore  # Now you can import unicore as usual


# Predicate function that might raise an exception
def safe_divide(x):
    return 10 / x == 2  # Will raise ZeroDivisionError if x == 0

array = [0, 1, 2, 5]

result = unicore.find(array, safe_divide)
print(result)  # Output: 5