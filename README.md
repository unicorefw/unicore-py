Unicore-py is a Python-based framework using UnicoreFW's Principles
===================================================================


# Unicore Framework
* * *
Bringing UnderscoreJS UX to other languages in a unified way. Our goal is to create a secure and performant framework or toolbelt that can be used across multiple programming languages without sacrificing security or performance. To achieve this, I suggest the following approach:

Installation
------------

1.  Clone the repository:
    
        git clone https://github.com/unicorefw/unicore-py.git
        cd unicore-py
    
2.  Ensure Python 3.x is installed on your system.
    
3.  Install any required dependencies (if applicable):
    
        pip install -r requirements.txt
    
**Categorize Functions:**
- `Array Functions`: Operations on arrays and collections.
- `Object Functions`: Manipulations and utilities for objects.
- `Utility Functions`: General-purpose functions.
- `Function Functions`: Higher-order functions that operate on other functions.
- `Chaining Functions`: Methods that support function chaining.

**Array Functions**
- `_.map` – Transforms an array's elements based on a function.
- `_.reduce` – Reduces an array to a single value using a function.
- `_.reduceRight` – Like - `_.reduce, but starts from the right.
- `_.find` – Returns the first value that matches a predicate.
- `_.filter` – Returns an array of values that match a predicate.
- `_.where` – Filters an array of objects, matching a set of key-value pairs.
- `_.findWhere` – Like - `_.where, but returns only the first match.
- `_.reject` – Returns an array of values that fail a predicate.
- `_.every` – Tests whether all values pass a predicate.
- `_.some` – Tests whether any values pass a predicate.
- `_.contains` – Checks if a value exists in an array.
- `_.invoke` – Invokes a method on every item in a collection.
- `_.pluck` – Extracts a list of values from an array of objects.
- `_.max` – Returns the maximum value based on a function.
- `_.min` – Returns the minimum value based on a function.
- `_.sortBy` – Sorts an array by a function's result.
- `_.groupBy` – Groups an array by the result of a function.
- `_.indexBy` – Indexes an array by a property value or function result.
- `_.countBy` – Counts instances of values by a function's result.
- `_.shuffle` – Shuffles the values in an array.
- `_.sample` – Selects random values from an array.
- `_.toArray` – Converts an iterable into an array.
- `_.size` – Returns the size of a collection.
- `_.partition` – Splits a collection into two arrays based on a predicate.
- `_.first` – Returns the first elements of an array.
- `_.initial` – Returns everything but the last element of an array.
- `_.last` – Returns the last elements of an array.
- `_.rest` – Returns everything but the first element of an array.
- `_.compact` – Removes falsey values from an array.
- `_.flatten` – Flattens a nested array.
- `_.without` – Returns an array with specified values removed.
- `_.uniq` – Removes duplicate values from an array.
- `_.union` – Combines arrays, removing duplicates.
- `_.intersection` – Returns values common to all arrays.
- `_.difference` – Returns values from the first array not present in others.
- `_.zip` – Merges arrays based on their index.
- `_.unzip` – Reverses the process of - `_.zip.
- `_.object` – Converts an array of pairs into an object.
- `_.range` – Creates an array of numbers in a range.
- `_.chunk` – Splits an array into chunks of a specified size.

**Object Functions**
- `_.keys` – Returns an array of an object's keys.
- `_.allKeys` – Returns an array of an object's keys, including inherited ones.
- `_.values` – Returns an array of an object's values.
- `_.mapObject` – Applies a function to each value of an object.
- `_.pairs` – Converts an object into an array of [key, value] pairs.
- `_.invert` – Inverts an object's keys and values.
- `_.functions` – Returns an array of all function property names in an object.
- `_.extend` – Extends an object with the properties of other objects.
- `_.extendOwn` – Like - `_.extend, but only copies own properties.
- `_.defaults` – Assigns default properties to an object.
- `_.create` – Creates an object with a specified prototype.
- `_.clone` – Creates a shallow copy of an object.
- `_.tap` – Invokes a function with an object and returns the object.
- `_.has` – Checks if an object contains a given property.
- `_.property` – Returns a function that retrieves a property value.
- `_.propertyOf` – Returns a function that retrieves a property value from a given object.
- `_.matcher (or - `_.matches)` – Creates a function that checks for matching key-value pairs.
- `_.isEqual` – Performs a deep comparison between objects.
- `_.isMatch` – Checks if an object matches key-value pairs.
- `_.isEmpty` – Checks if an object is empty.
- `_.isElement` – Checks if an object is a DOM element.
- `_.isArray` – Checks if a value is an array.
- `_.isObject` – Checks if a value is an object.
- `_.isArguments` – Checks if a value is an arguments object.
- `_.isFunction` – Checks if a value is a function.
- `_.isString` – Checks if a value is a string.
- `_.isNumber` – Checks if a value is a number.
- `_.isFinite` – Checks if a value is a finite number.
- `_.isBoolean` – Checks if a value is a boolean.
- `_.isDate` – Checks if a value is a date.
- `_.isRegExp` – Checks if a value is a regular expression.
- `_.isError` – Checks if a value is an error.
- `_.isSymbol` – Checks if a value is a symbol.
- `_.isMap` – Checks if a value is a map.
- `_.isWeakMap` – Checks if a value is a weak map.
- `_.isSet` – Checks if a value is a set.
- `_.isWeakSet` – Checks if a value is a weak set.
- `_.isNull` – Checks if a value is null.
- `_.isUndefined` – Checks if a value is undefined.
- `_.isNaN` – Checks if a value is NaN.
- `_.isTypedArray` – Checks if a value is a typed array.
- `_.isArrayBuffer` – Checks if a value is an array buffer.
- `_.isDataView` – Checks if a value is a data view.

**Utility Functions**
- `_.identity` – Returns the same value that is passed.
- `_.constant` – Returns a function that returns the given value.
- `_.noop` – A function that does nothing.
- `_.times` – Invokes a function a specified number of times.
- `_.random` – Returns a random number between a min and max.
- `_.mixin` – Adds functions to the Underscore object.
- `_.iteratee` – Returns a function that can be applied to each element in a collection.
- `_.uniqueId` – Generates a unique identifier.
- `_.escape` – Escapes a string for inclusion in HTML.
- `_.unescape` – Unescapes a string from HTML.
- `_.result` – Resolves the value of a property, potentially invoking it as a function.
- `_.now` – Returns the current timestamp.
- `_.template` – Compiles a template to a function.
- `_.chain` – Returns a wrapped object to allow chaining of functions.
- `_.value` – Extracts the result from a chained object.
  
**Function Functions**
- `_.bind` – Binds a function to an object.
- `_.partial` – Partially applies a function by pre-filling some arguments.
- `_.bindAll` – Binds methods of an object to the object itself.
- `_.memoize` – Caches the result of a function call.
- `_.delay` – Delays a function for a specified number of milliseconds.
- `_.defer` – Defers a function to be executed after the current call stack clears.
- `_.throttle` – Creates a throttled version of a function.
- `_.debounce` – Creates a debounced version of a function.
- `_.once` – Ensures a function is only called once.
- `_.after` – Returns a function that will only run after it has been called N times.
- `_.before` – Returns a function that will run until it has been called N times.
- `_.wrap` – Wraps a function inside another function.
- `_.negate` – Returns the negation of a predicate function.
- `_.compose` – Composes functions together to run in sequence.

**Chaining Functions**
- `_.chain` – Starts a chain.
- `_.value` – Extracts the value at the end of a chain.



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











Overview
--------

UnicoreFW-PY is a Python-based framework based on UnderscoreJS, designed to offer a comprehensive set of utilities and functional programming tools. This framework is equipped with command-line capabilities that allow users to execute example scripts, parse custom command-line arguments, and integrate powerful utility methods for various use cases. The goal of UnicoreFW is to provide security, performance, and ease of use for developers looking to build and maintain Python applications.

Features
--------

*   **Command-line Parsing**: Parse command-line arguments with `--name=value` syntax and support additional positional arguments.
    
*   **Flexible Test Execution**: Run example scripts through the command line for rapid prototyping and testing.
    
*   **Utility Functions**: Includes a robust set of utility methods for functional programming, string manipulation, and more.
    
*   **Secure Execution**: Built-in security measures to safely execute code and handle user inputs.
    


    

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
