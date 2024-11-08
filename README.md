UnicoreFW-PY is a Python-based framework 
==========================================

Overview
--------

UnicoreFW-PY is a Python-based framework based on UnderscoreJS, designed to offer a comprehensive set of utilities and functional programming tools. This framework is equipped with command-line capabilities that allow users to execute example scripts, parse custom command-line arguments, and integrate powerful utility methods for various use cases. The goal of UnicoreFW is to provide security, performance, and ease of use for developers looking to build and maintain Python applications.

Features
--------

*   **Command-line Parsing**: Parse command-line arguments with `--name=value` syntax and support additional positional arguments.
    
*   **Flexible Test Execution**: Run example scripts through the command line for rapid prototyping and testing.
    
*   **Utility Functions**: Includes a robust set of utility methods for functional programming, string manipulation, and more.
    
*   **Secure Execution**: Built-in security measures to safely execute code and handle user inputs.
    

Installation
------------

1.  Clone the repository:
    
        git clone https://github.com/unicorefw/unicore-py.git
        cd unicore-py
    
2.  Ensure Python 3.x is installed on your system.
    
3.  Install any required dependencies (if applicable):
    
        pip install -r requirements.txt
    

Directory Structure
-------------------

    project_root_dir/
    ├── src/
    │   └── unicore.py
    ├── examples/
    │   └── test.py
    └── README.md

Usage
-----

### Running the Command-Line Utility

The primary entry point for using UnicoreFW is through `test.py`, which provides command-line functionality.

Navigate to the project root and run:

    python examples/test.py --test=examples <method>

**Example Command**:

    python examples/test.py --test=examples example1

This command will execute `ex_example1.py` from the `examples/` directory.

### Parsing Command-Line Arguments

UnicoreFW includes a command-line argument parser that supports `--name=value` format with additional positional arguments.

**Example Usage**:

    python examples/test.py --name=John --verbose=true extra_arg1 extra_arg2

**Expected Output**:

    Parsed key-value pairs: {'name': 'John', 'verbose': 'true'}
    Positional arguments: ['extra_arg1', 'extra_arg2']

Example Code
------------

Here is a sample implementation using UnicoreFW's command-line parsing:

    # examples/test.py
    import sys
    import os
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
    from unicore import unicore
    
    # Run example functions
    unicore.some_function("Hello, World!")

Security Considerations
-----------------------

*   **Safe Execution**: The framework ensures that code execution is sandboxed and limited in scope to avoid unwanted side effects.
    
*   **Input Validation**: Command-line inputs are validated to prevent invalid or malicious commands.
    

Contributing
------------

We welcome contributions to UnicoreFW! Please follow these steps:

1.  Fork the repository.
    
2.  Create a feature branch.
    
3.  Submit a pull request with a detailed description of your changes.
    

License
-------

This project is licensed under the MIT License. See the LICENSE file for details.

Contact
-------

For any questions or feedback, please contact \[your email/contact\].

**PYTHON IMPLEMENTATION**
* * *
This class, `unicore`, provides a wide range of utility functions for working with arrays, objects, and strings. Here's a summary of what each method does:

**Array Functions:**

- `map(array, func)`: Applies a function to each element of an array and returns a new array.
- `filter(array, func)`: Filters elements in an array based on a predicate function.
- `reduce(array, func, initial=None)`: Reduces the array to a single value using the provided function.
- `find(array, func)`: Finds the first element in the array that matches a predicate function.
- `uniq(array)`: Removes duplicates from an array.
- `flatten(array, depth=float('inf'))`: Flattens a nested array into a one-dimensional array.
- `first(array, n=1)`: Returns the first n elements of an array.
- `last(array, n=1)`: Returns the last n elements of an array.
- `compact(array)`: Removes falsey values from an array.
- `without(array, *values)`: Returns an array excluding all provided values.
- `range(start, stop=None, step=1)`: Generates a range of numbers.
- `intersection(*arrays)`: Returns an array of values common to all arrays.
- `difference(array, *others)`: Returns values from the first array not present in others.
- `groupBy(array, key_func)`: Groups array elements by the result of a function.
- `sortBy(array, key_func)`: Sorts an array by a function or key.
- `sample(array, n=1)`: Returns a random sample from an array.
- `zip(*arrays)`: Combines multiple arrays into an array of tuples.
- `unzip(array_of_tuples)`: Separates tuples into arrays.

**Object Functions:**

- `keys(obj)`: Returns the keys of a dictionary.
- `values(obj)`: Returns the values of a dictionary.
- `extend(obj, *sources)`: Extends an object by copying properties from sources.
- `clone(obj)`: Creates a shallow copy of an object.
- `has(obj, key)`: Checks if an object has a given property key.
- `defaults(obj, defaults)`: Assigns default properties to an object if they are missing.
- `invert(obj)`: Inverts an object's keys and values.

**Type Checking Functions:**

- `isString(obj)`: Checks if an object is a string.
- `isNumber(obj)`: Checks if an object is a number.
- `isArray(obj)`: Checks if an object is a list.
- `isObject(obj)`: Checks if an object is a dictionary.
- `isFunction(obj)`: Checks if an object is callable.
- `isBoolean(obj)`: Checks if an object is a boolean.
- `isDate(obj)`: Checks if an object is a date object.
- `isRegExp(obj)`: Checks if an object is a regular expression.
- `isError(obj)`: Checks if an object is an error instance.
- `isNull(obj)`: Checks if an object is None.
- `isUndefined(obj)`: Checks if an object is undefined.
- `isFinite(obj)`: Checks if an object is a finite number.
- `isNaN(obj)`: Checks if an object is NaN.
- `isMap(obj)`: Checks if an object is a map.
- `isSet(obj)`: Checks if an object is a set.

**Utility Functions:**

- `identity(value)`: Returns the given value unchanged.
- `times(n, func)`: Calls a function n times.
- `uniqueId(prefix="")`: Generates a unique identifier with an optional prefix.
- `escape(string)`: Escapes HTML characters in a string.
- `unescape(string)`: Unescapes HTML characters in a string.
- `now()`: Returns the current timestamp.
- `memoize(func)`: Caches the results of function calls.
- `bind(func, context, *args)`: Binds a function to a context, optionally pre-filling arguments.
- `partial(func, *partial_args)`: Partially applies arguments to a function.
- `throttle(func, wait)`: Throttles a function to be called at most once every wait milliseconds.
- `debounce(func, wait)`: Debounces a function to only be called after wait milliseconds.
- `once(func)`: Ensures a function is only called once.
- `after(times, func)`: Returns a function that will only run after it's been called a specified number of times.
- `compose(*funcs)`: Composes multiple functions to execute in sequence.
- `invoke(array, func_name, *args)`: Calls a method on each item in an array.
- `matches(attrs)`: Returns a function that checks if an object matches key-value pairs.
- `allKeys(obj)`: Returns all keys of an object, including inherited ones
