########################################################################
# UniCoreFW - Universal Core Utility Library                           #
# Copyright (C) 2024 Kenny Ngo / UnicoreFW / IIPTech.info              #
#                                                                      #
# This file is part of UniCoreFW.                                      #
# UniCore is free software: you can redistribute it and/or modify      #
# it under the terms of the [LGPL-3.0/MPL-2.0] as published by         #
# the Free Software Foundation.                                        #
# You should have received a copy of the [LGPL-3.0/MPL-2.0] license    #
# along with UniCoreFW. If not, see https://www.gnu.org/licenses/.     #
########################################################################

import re
import random
import threading

class unicore:
    _id_counter = 0  # Initialize the counter

    # -------- Extended Functions -------- #
    @staticmethod
    def findMedianSortedArrays(nums1, nums2):
        '''
        Finds the median of two sorted arrays using binary search.

        This function uses binary search to find the median of two sorted arrays, nums1 and nums2.
        It ensures that nums1 is the smaller array for efficiency.

        The time complexity for this function is O(log(min(m, n))), where m and n are the lengths
        of nums1 and nums2, respectively.

        The space complexity for this function is O(1), since it only uses a constant amount of space.

        Parameters:
        nums1 (list): The first sorted array.
        nums2 (list): The second sorted array.

        Returns:
        float: The median of the two sorted arrays.
        '''
        # Ensure nums1 is the smaller array for binary search efficiency
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total_length = m + n
        half_length = (total_length + 1) // 2  # For handling both odd/even cases

        left, right = 0, m

        while left <= right:
            partition1 = (left + right) // 2
            partition2 = half_length - partition1

            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]

            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else nums2[partition2]

            # Check if we've partitioned correctly
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # If odd, return the max of the left halves
                if total_length % 2 == 1:
                    return max(maxLeft1, maxLeft2)
                # If even, return the average of the two middle values
                return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
            elif maxLeft1 > minRight2:
                # Move towards left in nums1
                right = partition1 - 1
            else:
                # Move towards right in nums1
                left = partition1 + 1

    @staticmethod
    def decompress(comp):
        '''
        Decompresses a given string, which is compressed using run-length encoding.

        The compressed string is given as a parameter, and the function will return the decompressed string.

        For example, if the input string is "3(a)2(b)3(c)", the output will be "aaabbccc".

        :param comp: The compressed string to be decompressed.
        :return: The decompressed string.
        '''
        result = []
        i = 0

        while i < len(comp):
            # Extract the number (count of characters)
            count = 0
            while i < len(comp) and comp[i].isdigit():
                count = count * 10 + int(comp[i])  # Handle multi-digit counts
                i += 1
            
            # Extract the character
            if i < len(comp):
                char = comp[i]
                result.append(char * count)  # Append repeated character
                i += 1

        return ''.join(result)

    @staticmethod
    def compress(word):
        """
        Compresses a string using a simple run-length encoding.

        This method compresses the input string by replacing sequences of repeated characters 
        with a single instance of the character followed by a number indicating the count 
        of repetitions. The count is capped at 9 to avoid ambiguity in decoding.

        Parameters:
        word (str): The input string to be compressed.

        Returns:
        str: A compressed version of the input string using run-length encoding.
        """
        if not word:
            return ""

        comp = []  # Use a list for faster concatenation
        length = len(word)
        i = 0

        while i < length:
            count = 1
            # Count up to 9 consecutive characters
            while i + count < length and word[i] == word[i + count] and count < 9:
                count += 1
            
            # Append the count and character to comp
            comp.append(f"{count}{word[i]}")
            
            # Move to the next distinct character
            i += count

        return ''.join(comp)  # Join the list into a single string at the end

    # -------- Array Functions -------- #
    @staticmethod
    def map(array, func):
        """Applies func to each element of the array and returns a new array."""
        return [func(x) for x in array]

    @staticmethod
    def reduce(array, func, initial=None):
        """Reduces the array to a single value using the func and an optional initial value."""
        result = initial
        for x in array:
            if result is None:
                result = x
            else:
                result = func(result, x)
        return result

    def find(array, func):
        """
        Finds the first element in the array that matches the predicate func.

        Security Considerations:
            - Validates inputs to prevent type-related errors.
            - Catches and handles exceptions raised by func(x).
            - Avoids modifying the input array.
        """
        # Input validation
        if not hasattr(array, '__iter__'):
            raise TypeError("The 'array' parameter must be iterable.")
        if not callable(func):
            raise TypeError("The 'func' parameter must be callable.")

        for x in array:
            try:
                if func(x):
                    return x
            except Exception:
                # Handle exceptions securely
                # Optionally log the exception without exposing sensitive information
                continue  # Skip elements that cause exceptions
        return None

    @staticmethod
    def uniq(array):
        """Removes duplicates from the array."""
        return list(set(array))

    @staticmethod
    def first(*args, **kwargs):
        """
        Returns the first element of an array or the first n elements if specified.

        Parameters:
            *args: The array or array elements, and possibly n.
            **kwargs: Optional keyword argument 'n'.

        Behavior:
            - If the first argument is a list or tuple, and the second argument is an integer,
              the second argument is treated as 'n'.
            - If multiple positional arguments are given and the first argument is not a list or tuple,
              they are treated as array elements.
            - 'n' can also be provided as a keyword argument.

        Returns:
            The first element or first n elements of the array.
        """
        n = kwargs.get('n', None)
        args_len = len(args)

        if args_len == 0:
            return None if n is None else []

        array = args[0] if args_len == 1 else args

        if isinstance(array, (list, tuple)):
            if n is None:
                return array[0] if array else None
            if not isinstance(n, int) or n <= 0:
                return []
            return array[:n]

        if args_len >= 2 and isinstance(args[1], int):
            array, n = args[0], args[1]

        if n is None:
            return array
        if not isinstance(n, int) or n <= 0:
            return []
        return [array][:n]

    @staticmethod
    def last(array, n=None):
        """Returns the last element of an array or the last n elements if specified."""
        # Handle case where array is None
        if array is None:
            return None if n is None else []

        if not array:
            return None if n is None else []
        
        if n is None:
            return array[-1]
        elif n <= 0:
            return []
        else:
            return array[-n:]
        
    @staticmethod
    def compact(array):
        """Removes falsey values from an array."""
        return [x for x in array if x]

    @staticmethod
    def without(array, *values):
        """Returns an array excluding all provided values."""
        return [x for x in array if x not in values]
    
    @staticmethod
    def pluck(array, key):
        """Extracts a list of property values from an array of objects."""
        return [obj.get(key) if isinstance(obj, dict) else getattr(obj, key, None) for obj in array]

    @staticmethod
    def shuffle(array):
        """Randomly shuffles the values in an array."""
        # Use the Fisher-Yates shuffle algorithm, which is secure and efficient
        array_copy = list(array)
        for i in range(len(array_copy) - 1, 0, -1):
            j = random.randint(0, i)
            array_copy[i], array_copy[j] = array_copy[j], array_copy[i]
        return array_copy

    @staticmethod
    def zip(*arrays):
        """Combines multiple arrays into an array of tuples."""
        return list(zip(*arrays))

    @staticmethod
    def unzip(array_of_tuples):
        """Reverses the zip operation by separating tuples into arrays."""
        return list(map(list, zip(*array_of_tuples)))

    @staticmethod
    def partition(array, predicate):
        """Splits the array into two arrays: one matching the predicate and one that doesn't."""
        return ([x for x in array if predicate(x)], [x for x in array if not predicate(x)])

    @staticmethod
    def lastIndexOf(array, value):
        """Returns the last index of a specified value in an array."""
        for i in range(len(array) - 1, -1, -1):
            if array[i] == value:
                return i
        return -1

    # -------- Object Functions -------- #
    @staticmethod
    def keys(obj):
        """Returns the keys of a dictionary."""
        return list(obj.keys())

    @staticmethod
    def values(obj):
        """Returns the values of a dictionary."""
        return list(obj.values())

    @staticmethod
    def extend(obj, *sources):
        """Extends obj by copying properties from sources."""
        for source in sources:
            obj.update(source)
        return obj

    @staticmethod
    def clone(obj):
        """Creates a shallow copy of an object (dictionary or list)."""
        if isinstance(obj, dict):
            return obj.copy()
        elif isinstance(obj, list):
            return list(obj)
        else:
            return obj

    @staticmethod
    def has(obj, key):
        """Checks if obj has a given property key."""
        return key in obj

    @staticmethod
    def invert(obj):
        """Inverts an object's keys and values."""
        return {v: k for k, v in obj.items()}

    def defaults(obj, *defaults):
        """
        Assigns default properties to obj if they are missing.

        Parameters:
            obj (dict): The original dictionary to update.
            *defaults (dict): One or more dictionaries containing default values.

        Returns:
            dict: A new dictionary with defaults applied.

        Security Considerations:
            - Validates that 'obj' and 'defaults' are dictionaries.
            - Checks that keys in 'defaults' are strings.
            - Does not modify 'obj' in-place to prevent unintended side effects.
        """
        if not isinstance(obj, dict):
            raise TypeError("The 'obj' parameter must be a dictionary.")

        # Create a copy to avoid modifying the original object
        result = obj.copy()

        for default in defaults:
            if not isinstance(default, dict):
                raise TypeError("Each default must be a dictionary.")
            for key, value in default.items():
                if key not in obj:
                        obj[key] = value
                if not isinstance(key, str):
                    raise ValueError("Keys in defaults must be strings.")
                # Only set the default if the key is not already in 'result'
                if key not in result:
                    result[key] = value
        return result
    
    @staticmethod
    def create(proto, properties=None):
        """Creates an object with proto as its prototype, with optional properties."""
        class PrototypeBasedObject(proto.__class__):
            pass
        instance = PrototypeBasedObject()
        instance.__dict__ = proto.__dict__.copy()
        if properties:
            instance.__dict__.update(properties)
        return instance

    @staticmethod
    def pairs(obj):
        """Converts an object into an array of [key, value] pairs."""
        return list(obj.items())

    @staticmethod
    def result(obj, property_name, *args):
        """If the property is a function, invoke it with args; otherwise, return the property value."""
        value = obj.get(property_name)
        
        if callable(value):
            # Directly call the function with args if it's callable
            return value(*args)
        
        return value

    @staticmethod
    def size(obj):
        """Returns the number of values in obj (works for dicts, lists, etc.)."""
        if hasattr(obj, '__len__'):
            return len(obj)
        return sum(1 for _ in obj)

    @staticmethod
    def toArray(obj):
        """Converts obj into an array (list in Python)."""
        if isinstance(obj, list):
            return obj
        elif isinstance(obj, (dict, set)):
            return list(obj.values()) if isinstance(obj, dict) else list(obj)
        elif hasattr(obj, '__iter__'):
            return list(obj)
        return [obj]

    @staticmethod
    def where(obj_list, properties):
        """Returns an array of all objects in obj_list that match the key-value pairs in properties."""
        return [obj for obj in obj_list if all(obj.get(k) == v for k, v in properties.items())]

    @staticmethod
    def object(pairs):
        """Converts a list of [key, value] pairs into an object."""
        return {k: v for k, v in pairs}
    
    # -------- Type Checking -------- #
    @staticmethod
    def isString(obj):
        """Checks if obj is a string."""
        return isinstance(obj, str)

    @staticmethod
    def isNumber(obj):
        """Checks if obj is a number (int or float)."""
        return isinstance(obj, (int, float))

    @staticmethod
    def isArray(obj):
        """Checks if obj is a list."""
        return isinstance(obj, list)

    @staticmethod
    def isObject(obj):
        """Checks if obj is a dictionary."""
        return isinstance(obj, dict)

    @staticmethod
    def isFunction(obj):
        """Checks if obj is callable (function)."""
        return callable(obj)

    @staticmethod
    def isBoolean(obj):
        """Checks if obj is a boolean."""
        return isinstance(obj, bool)

    @staticmethod
    def isDate(obj):
        """Checks if obj is a date object."""
        from datetime import date
        return isinstance(obj, date)

    @staticmethod
    def isRegExp(obj):
        """Checks if obj is a regular expression."""
        return isinstance(obj, re.Pattern)

    @staticmethod
    def isError(obj):
        """Checks if obj is an error instance."""
        return isinstance(obj, Exception)
    
    @staticmethod
    def isNull(obj):
        """Checks if obj is None."""
        return obj is None

    @staticmethod
    def isUndefined(obj):
        """Checks if obj is undefined (None in Python)."""
        return obj is None

    @staticmethod
    def isFinite(obj):
        """Checks if obj is a finite number."""
        from math import isfinite
        return isinstance(obj, (int, float)) and isfinite(obj)

    @staticmethod
    def isNaN(obj):
        """Checks if obj is NaN."""
        from math import isnan
        return isinstance(obj, float) and isnan(obj)

    @staticmethod
    def isMap(obj):
        """Checks if obj is a map."""
        return isinstance(obj, dict)

    @staticmethod
    def isSet(obj):
        """Checks if obj is a set."""
        return isinstance(obj, set)
    @staticmethod
    def isArguments(obj):
        """Checks if obj is an arguments object (useful in JavaScript, not directly applicable in Python)."""
        # Since Python doesn't have a direct "arguments" object, we check if obj is a tuple,
        # which is a common way to represent function arguments in Python.
        return isinstance(obj, tuple)

    @staticmethod
    def isArrayBuffer(obj):
        """Checks if obj is an ArrayBuffer. In Python, we approximate with bytearray."""
        return isinstance(obj, (bytearray, memoryview))

    @staticmethod
    def isDataView(obj):
        """Checks if obj is a DataView. In Python, memoryview is similar to a DataView in JavaScript."""
        return isinstance(obj, memoryview)

    @staticmethod
    def isTypedArray(obj):
        """Checks if obj is a typed array. In Python, we approximate with array.array."""
        from array import array
        return isinstance(obj, array)

    @staticmethod
    def isWeakMap(obj):
        """Checks if obj is a WeakMap. Python equivalent is weakref.WeakKeyDictionary."""
        from weakref import WeakKeyDictionary
        return isinstance(obj, WeakKeyDictionary)

    @staticmethod
    def isWeakSet(obj):
        """Checks if obj is a WeakSet. Python equivalent is weakref.WeakSet."""
        from weakref import WeakSet
        return isinstance(obj, WeakSet)

    @staticmethod
    def isElement(obj):
        """Checks if obj is a DOM element. This is browser-specific, so in Python, we can check for an ElementTree element."""
        try:
            from xml.etree.ElementTree import Element
            return isinstance(obj, Element)
        except ImportError:
            return False

    @staticmethod
    def isEmpty(obj):
        """Checks if an object is empty."""
        if obj is None:
            return True
        if hasattr(obj, '__len__'):
            return len(obj) == 0
        if hasattr(obj, '__iter__'):
            return not any(True for _ in obj)
        return False

    @staticmethod
    def isMatch(obj, attrs):
        """Checks if obj has key-value pairs that match attrs."""
        return all(obj.get(k) == v for k, v in attrs.items())

    @staticmethod
    def isSymbol(obj):
        """Checks if obj is a symbol. Python doesn't have symbols, so we check for other unique constant objects."""
        # In Python, symbols aren't common, so here we return False unless it’s a unique constant type.
        return isinstance(obj, (type(None), type(NotImplemented), type(Ellipsis)))

    # -------- Utility Functions -------- #
    @staticmethod
    def identity(value):
        """Returns the given value unchanged."""
        return value

    @staticmethod
    def times(n, func):
        """Calls a function n times."""
        return [func(i) for i in range(n)]

    @staticmethod
    def uniqueId(prefix=""):
        """Generates a unique identifier with an optional prefix."""
        unicore._id_counter += 1
        return f"{prefix}{unicore._id_counter}"

    @staticmethod
    def escape(string):
        """Escapes HTML characters in a string."""
        escape_map = {
            "&": "&amp;",
            "<": "&lt;",
            ">": "&gt;",
            '"': "&quot;",
            "'": "&#x27;",
            "`": "&#x60;"
        }
        return "".join(escape_map.get(c, c) for c in string)

    @staticmethod
    def unescape(string):
        """Unescapes HTML characters in a string."""
        unescape_map = {
            "&amp;": "&",
            "&lt;": "<",
            "&gt;": ">",
            "&quot;": '"',
            "&#x27;": "'",
            "&#x60;": "`"
        }
        for key, value in unescape_map.items():
            string = string.replace(key, value)
        return string

    @staticmethod
    def now():
        """Returns the current timestamp."""
        from time import time
        return int(time() * 1000)

    @staticmethod
    def memoize(func):
        """Caches the results of function calls."""
        cache = {}
        def memoized_func(*args):
            if args not in cache:
                cache[args] = func(*args)
            return cache[args]
        return memoized_func
    
    # -------- Function Utilities -------- #
    @staticmethod
    def partial(func, *partial_args):
        """Partially applies arguments to a function."""
        def partially_applied(*extra_args):
            return func(*(partial_args + extra_args))
        return partially_applied

    @staticmethod
    def throttle(func, wait):
        """Throttles a function to be called at most once every wait milliseconds."""
        import time
        last_called = [0]
        
        def throttled_func(*args, **kwargs):
            now = time.time()
            if now - last_called[0] > wait / 1000:
                last_called[0] = now
                return func(*args, **kwargs)
        
        return throttled_func

    @staticmethod
    def debounce(func, wait, *, use_main_thread=False):
        """
        Debounces a function to only be called after wait milliseconds.

        Parameters:
            func (callable): The function to debounce.
            wait (int): The delay in milliseconds.
            use_main_thread (bool): If True, ensures `func` is called in the main thread.

        Returns:
            callable: The debounced function.
        """
        wait_seconds = wait / 1000.0
        timer = None
        lock = threading.Lock()

        def debounced(*args, **kwargs):
            nonlocal timer
            def call_func():
                if use_main_thread:
                    # Queue the function to be called in the main thread
                    threading.main_thread().run(func, *args, **kwargs)
                else:
                    func(*args, **kwargs)

            with lock:
                if timer is not None:
                    timer.cancel()
                timer = threading.Timer(wait_seconds, call_func)
                timer.start()

        return debounced

    @staticmethod
    def once(func):
        """Ensures a function is only called once, returning None on subsequent calls."""
        result = [None]
        has_been_called = [False]

        def once_func(*args, **kwargs):
            if not has_been_called[0]:
                result[0] = func(*args, **kwargs)
                has_been_called[0] = True
            else:
                result[0] = None  # Return None after the first call
            return result[0]
        return once_func

    @staticmethod
    def after(times, func):
        """Returns a function that will only run after it's been called a specified number of times."""
        calls = [0]
        
        def after_func(*args, **kwargs):
            calls[0] += 1
            if calls[0] >= times:
                return func(*args, **kwargs)
        
        return after_func

    @staticmethod
    def compose(*funcs):
        """Composes multiple functions to execute in sequence."""
        def composed(value):
            for func in reversed(funcs):
                value = func(value)
            return value
        return composed

    @staticmethod
    def invoke(array, func_name, *args):
        """Calls a method on each item in an array."""
        return [getattr(item, func_name)(*args) if hasattr(item, func_name) else None for item in array]

    @staticmethod
    def matches(attrs):
        """Returns a function that checks if an object matches key-value pairs."""
        def match(obj):
            return all(obj.get(k) == v for k, v in attrs.items())
        return match

    @staticmethod
    def allKeys(obj):
        """Returns all keys of an object, including inherited ones."""
        keys = set()
        for k in dir(obj):
            keys.add(k)
        return list(keys)
    
    @staticmethod
    def bind(func, context, *args):
        """Binds a function to a context with optional pre-filled arguments."""
        def bound_func(*extra_args):
            return func(*(args + extra_args))  # Only pass args and extra_args without context
        return bound_func
    
    # -------- Advanced Array Functions -------- #
    @staticmethod
    def sortBy(array, key_func):
        """Sorts an array by a function or key."""
        return sorted(array, key=key_func)

    @staticmethod
    def groupBy(array, key_func):
        """Groups array elements by the result of a function."""
        if not hasattr(array, '__iter__'):
            raise TypeError("The 'array' parameter must be iterable.")
        if not callable(key_func):
            raise TypeError("The 'key_func' parameter must be callable.")
        grouped = {}
        for item in array:
            try:
                key = key_func(item)
                grouped.setdefault(key, []).append(item)
            except Exception:
                # Handle exceptions securely
                # Optionally log the exception without exposing sensitive information
                continue  # Skip elements that cause exceptions
        return grouped

    # -------- Deep Comparison -------- #
    @staticmethod
    def isEqual(obj1, obj2):
        """Performs a deep comparison between two objects for equality."""
        if type(obj1) != type(obj2):
            return False
        if isinstance(obj1, dict):
            if len(obj1) != len(obj2):
                return False
            return all(k in obj2 and unicore.isEqual(v, obj2[k]) for k, v in obj1.items())
        elif isinstance(obj1, list):
            if len(obj1) != len(obj2):
                return False
            return all(unicore.isEqual(x, y) for x, y in zip(obj1, obj2))
        return obj1 == obj2

    # -------- Helpers and Miscellaneous -------- #
    @staticmethod
    def noop():
        """A function that does nothing (no operation)."""
        pass

    @staticmethod
    def constant(value):
        """Returns a function that always returns the specified value."""
        return lambda: value

    @staticmethod
    def random(min_val, max_val):
        """Returns a random integer between min_val and max_val, inclusive."""
        from random import randint
        return randint(min_val, max_val)

    @staticmethod
    def some(array, func):
        """Checks if at least one element in the array matches the predicate."""
        return any(func(x) for x in array)

    @staticmethod
    def every(array, func):
        """Checks if every element in the array matches the predicate."""
        return all(func(x) for x in array)

    @staticmethod
    def wrap(func, wrapper):
        """Wraps a function inside a wrapper function."""
        def wrapped(*args, **kwargs):
            return wrapper(func, *args, **kwargs)
        return wrapped

    @staticmethod
    def iteratee(value):
        """Returns a function based on the type of value (identity if callable, otherwise a matcher)."""
        if callable(value):
            return value
        elif isinstance(value, dict):
            return lambda obj: all(obj.get(k) == v for k, v in value.items())
        else:
            return lambda obj: obj == value

    @staticmethod
    def max(array, key_func=None):
        """Returns the maximum value in the array, based on an optional key function."""
        if not array:
            return None
        if key_func:
            return max(array, key=key_func)
        return max(array)

    @staticmethod
    def min(array, key_func=None):
        """Returns the minimum value in the array, based on an optional key function."""
        if not array:
            return None
        if key_func:
            return min(array, key=key_func)
        return min(array)

    @staticmethod
    def mixin(obj):
        """Adds properties of obj as functions on unicore itself."""
        for key, func in obj.items():
            if callable(func):
                setattr(unicore, key, func)

    @staticmethod
    def chain(obj):
        """Enables chaining by wrapping the object in a chainable class."""
        class Chained:
            def __init__(self, obj):
                self._wrapped = obj

            def value(self):
                return self._wrapped

            def __getattr__(self, attr):
                func = getattr(unicore, attr)
                if callable(func):
                    def chainable(*args, **kwargs):
                        result = func(self._wrapped, *args, **kwargs)
                        if result is None:
                            return self
                        return Chained(result)
                    return chainable
                raise AttributeError(f"{attr} is not a valid attribute")
                
        return Chained(obj)
    
    @staticmethod
    def tap(value, func):
        """Invokes func with the value and then returns value."""
        func(value)
        return value
    
    # -------- Utility and Array Functions -------- #
    @staticmethod
    def chunk(array, size):
        """Splits an array into chunks of specified size."""
        return [array[i:i + size] for i in range(0, len(array), size)]

    @staticmethod
    def initial(array, n=1):
        """Returns all elements except the last n elements."""
        return array[:-n] if n < len(array) else []

    @staticmethod
    def rest(array, n=1):
        """Returns all elements except the first n elements."""
        return array[n:]

    @staticmethod
    def contains(array, value):
        """Checks if a value is present in the array."""
        return value in array

    def flatten(array, depth=None):
        """Flattens a nested array up to the specified depth."""
        if not isinstance(array, list):
            raise TypeError("Input must be a list.")

        if depth is None:
            depth = float('inf')
        elif not isinstance(depth, int) or depth < 0:
            raise ValueError("Depth must be a non-negative integer or None.")

        result = []

        def _flatten(arr, current_depth):
            for item in arr:
                if isinstance(item, list) and current_depth > 0:
                    _flatten(item, current_depth - 1)
                else:
                    result.append(item)

        _flatten(array, depth)
        return result

    @staticmethod
    def reject(array, predicate):
        """The opposite of filter; returns items that do not match the predicate."""
        return [x for x in array if not predicate(x)]

    @staticmethod
    def filter(array, func):
        """Filters elements in array based on func predicate."""
        return [x for x in array if func(x)]

    @staticmethod
    def sample(array, n=1):
        """Returns a random sample from an array."""
        from random import sample
        return sample(array, n if n < len(array) else len(array))

    @staticmethod
    def indexBy(array, key_func):
        """Creates an index of array elements by a key function."""
        return {key_func(item): item for item in array}

    @staticmethod
    def countBy(array, key_func):
        """Counts instances in an array based on a function's result."""
        if not hasattr(array, '__iter__'):
            raise TypeError("The 'array' parameter must be iterable.")
        if not callable(key_func):
            raise TypeError("The 'key_func' parameter must be callable.")
        counts = {}
        for item in array:
            try:
                key = key_func(item)
                counts[key] = counts.get(key, 0) + 1
            except Exception:
                # Handle exceptions securely
                # Optionally log the exception without exposing sensitive information
                continue  # Skip elements that cause exceptions
        return counts
    
    # -------- Additional Utility Functions -------- #
    @staticmethod
    def negate(func):
        """Returns the negation of a predicate function."""
        return lambda *args, **kwargs: not func(*args, **kwargs)

    @staticmethod
    def property(prop_name):
        """Returns a function that retrieves a property value by name."""
        return lambda obj: obj.get(prop_name) if isinstance(obj, dict) else getattr(obj, prop_name, None)

    @staticmethod
    def propertyOf(obj):
        """Returns a function that retrieves a property value from a given object."""
        return lambda prop_name: obj.get(prop_name) if isinstance(obj, dict) else getattr(obj, prop_name, None)

    @staticmethod
    def matcher(attrs):
        """Returns a function that checks if an object has matching key-value pairs."""
        def match(obj):
            return all(obj.get(k) == v for k, v in attrs.items())
        return match

    @staticmethod
    def difference(array, *others):
        """Returns values from the first array not present in others."""
        other_elements = set().union(*others)
        return [x for x in array if x not in other_elements]

    @staticmethod
    def range(start, stop=None, step=1):
        """Generates an array of numbers in a range."""
        if stop is None:
            start, stop = 0, start
        return list(range(start, stop, step))

    @staticmethod
    def union(*arrays):
        """Combines arrays and removes duplicates."""
        return list(set().union(*arrays))

    @staticmethod
    def intersection(*arrays):
        """Returns an array of values common to all arrays."""
        common_elements = set(arrays[0])
        for arr in arrays[1:]:
            common_elements.intersection_update(arr)
        return list(common_elements)
    
    @staticmethod
    def before(n, func):
        """Returns a function that can be called up to n times."""
        result = [None]
        calls = [0]

        def limited_func(*args, **kwargs):
            if calls[0] < n:
                result[0] = func(*args, **kwargs)
                calls[0] += 1
            return result[0]
        
        return limited_func

    @staticmethod
    def bindAll(obj, *methodNames):
        """Binds specified methods of obj to obj itself."""
        for method_name in methodNames:
            if hasattr(obj, method_name):
                bound_method = getattr(obj, method_name).__get__(obj)
                setattr(obj, method_name, bound_method)

    @staticmethod
    def defer(func, *args, **kwargs):
        """Defers invoking the function until the current call stack has cleared."""
        threading.Timer(0, func, args=args, kwargs=kwargs).start()

    @staticmethod
    def delay(func, wait, *args, **kwargs):
        """Invokes func after a specified number of milliseconds."""
        threading.Timer(wait / 1000, func, args=args, kwargs=kwargs).start()

    @staticmethod
    def functions(obj):
        """Returns a list of names of functions on the obj."""
        return [name for name, val in obj.__class__.__dict__.items() if callable(val)]

    @staticmethod
    def mapObject(obj, func):
        """Applies func to each value in obj, returning a new object with the transformed values."""
        return {k: func(v) for k, v in obj.items()}

    @staticmethod
    def template(template, context):
        token_pattern = r'(<%=?[^%]*?%>)'
        def tokenize(template):
            tokens = re.split(token_pattern, template)
            return tokens
        
        def evaluate_expression(expr, context):
            # Allow simple variable access and method calls
            pattern = r'^([a-zA-Z_][a-zA-Z0-9_]*)(\.[a-zA-Z_][a-zA-Z0-9_]*(\(\))?)*$'
            if not re.match(pattern, expr):
                raise ValueError(f"Invalid expression: '{expr}'")

            parts = expr.split('.')
            value = context.get(parts[0], None)
            if value is None:
                raise NameError(f"Name '{parts[0]}' is not defined.")

            for part in parts[1:]:
                if part.endswith('()'):
                    method_name = part[:-2]
                    value = call_safe_method(value, method_name)
                else:
                    if hasattr(value, part):
                        value = getattr(value, part)
                    else:
                        raise AttributeError(f"Attribute '{part}' not found.")
            return value
    
        def evaluate_condition(condition, context):
            # Allow simple variable truthiness checks
            pattern = r'^([a-zA-Z_][a-zA-Z0-9_]*)$'
            if not re.match(pattern, condition):
                raise ValueError(f"Invalid condition: '{condition}'")

            value = context.get(condition, None)
            return bool(value)
        
        def call_safe_method(obj, method_name):
            # Only allow safe methods on strings
            safe_methods = {'upper', 'lower', 'title', 'capitalize'}
            if isinstance(obj, str) and method_name in safe_methods:
                method = getattr(obj, method_name)
                return method()
            else:
                raise ValueError(f"Method '{method_name}' is not allowed on object of type '{type(obj).__name__}'.")

        def evaluate_condition(condition, context):
            # Allow simple variable truthiness checks
            pattern = r'^([a-zA-Z_][a-zA-Z0-9_]*)$'
            if not re.match(pattern, condition):
                raise ValueError(f"Invalid condition: '{condition}'")

            value = context.get(condition, None)
            return bool(value)
        
        tokens = tokenize(template)
        output = ''
        skip_stack = []
        idx = 0

        while idx < len(tokens):
            token = tokens[idx]
            #token = token.strip('\n')
            if token.startswith('<%=') and token.endswith('%>'):
                if not any(skip_stack):
                    expr = token[3:-2].strip()
                    value = evaluate_expression(expr, context)
                    output += str(value)
            elif token.startswith('<%') and token.endswith('%>'):
                tag_content = token[2:-2].strip()
                if tag_content.startswith('if '):
                    condition = tag_content[3:].rstrip(':').strip()
                    result = evaluate_condition(condition, context)
                    skip_stack.append(not result)
                elif tag_content == 'endif':
                    if skip_stack:
                        skip_stack.pop()
                    else:
                        raise ValueError("Unmatched 'endif' found.")
                else:
                    raise ValueError(f"Unknown tag '{tag_content}'.")
            else:
                if not any(skip_stack):
                    output += token
            idx += 1

        if skip_stack:
            raise ValueError("Unclosed 'if' statement detected.")
        return output

    # TODO: Chain needs more methods
    @staticmethod
    def deep_copy(obj):
        """Creates a deep copy of the given object without using imports."""
        if isinstance(obj, dict):
            return {k: unicore.deep_copy(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [unicore.deep_copy(elem) for elem in obj]
        elif isinstance(obj, tuple):
            return tuple(unicore.deep_copy(elem) for elem in obj)
        elif isinstance(obj, str):
            # Strings are immutable, return as is
            return obj
        else:
            # For immutable objects like int, float, return as is
            return obj

    @staticmethod
    def chain(obj):
        """Starts a chain of operations on the given object."""
        class ChainInstance:
            def __init__(self, obj):
                self._value = unicore.deep_copy(obj)

            def value(self):
                """Extracts the value of the wrapped object."""
                return self._value

            def map(self, func):
                """Applies a function to each item of the list or string."""
                if isinstance(self._value, list):
                    self._value = [func(item) for item in self._value]
                elif isinstance(self._value, str):
                    self._value = ''.join([func(char) for char in self._value])
                else:
                    raise TypeError("The 'map' method is only applicable to lists and strings.")
                return self  # Return self to allow chaining

            def sortBy(self, key_func=None):
                """Sorts the list or string based on a key function."""
                if isinstance(self._value, list):
                    self._value.sort(key=key_func)
                elif isinstance(self._value, str):
                    # Convert string to list of characters, sort, then join back
                    sorted_chars = sorted(self._value, key=key_func)
                    self._value = ''.join(sorted_chars)
                else:
                    raise TypeError("The 'sortBy' method is only applicable to lists and strings.")
                return self
            
            def filter(self, func):
                """Filters the list or string based on a function."""
                if isinstance(self._value, list):
                    self._value = [item for item in self._value if func(item)]
                elif isinstance(self._value, str):
                    self._value = ''.join([char for char in self._value if func(char)])
                else:
                    raise TypeError("The 'filter' method is only applicable to lists and strings.")
                return self

            def first(self, n=1):
                """Returns the first element(s) of the list or string."""
                if isinstance(self._value, list):
                    if n == 1:
                        self._value = self._value[0] if self._value else None
                    else:
                        self._value = self._value[:n]
                elif isinstance(self._value, str):
                    if n == 1:
                        self._value = self._value[0] if self._value else ''
                    else:
                        self._value = self._value[:n]
                else:
                    raise TypeError("The 'first' method is only applicable to lists and strings.")
                return self

            def reverse(self):
                """Reverses the list or string."""
                if isinstance(self._value, list) or isinstance(self._value, str):
                    self._value = self._value[::-1]
                else:
                    raise TypeError("The 'reverse' method is only applicable to lists and strings.")
                return self

        return ChainInstance(obj)