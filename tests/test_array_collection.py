import sys
import os
import unittest

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from unicore import unicore  # Now you can import unicore as usual

class Testunicore(unittest.TestCase):

    # ------- Array and Collection Functions ------- #
    def test_first(self):
        self.assertEqual(unicore.first([1, 2, 3]), 1, 'can pull out the first element of an array')
        self.assertEqual(unicore.first([1, 2, 3]), 1, 'can perform OO-style "first()"')
        self.assertEqual(unicore.first([1, 2, 3], 0), [], 'returns an empty array when n <= 0 (0 case)')
        self.assertEqual(unicore.first([1, 2, 3], -1), [], 'returns an empty array when n <= 0 (negative case)')
        self.assertEqual(unicore.first([1, 2, 3], 2), [1, 2], 'can fetch the first n elements')
        self.assertEqual(unicore.first([1, 2, 3], 5), [1, 2, 3], 'returns the whole array if n > length')
        result = (lambda: unicore.first(4, 3, 2, 1))()
        self.assertEqual(result, 4, 'works on an arguments object')
        result = unicore.map([[1, 2, 3], [], [1, 2, 3]], lambda x: unicore.first(x))
        self.assertEqual(list(result), [1, None, 1], 'works well with unicore.map')
        self.assertEqual(unicore.first(None), None, 'returns undefined when called on null')
        self.assertEqual(unicore.first([], 10), [], 'returns an empty array when called with an explicit number of elements to return')
        self.assertEqual(unicore.first([], 1), [], 'returns an empty array when called with an explicit number of elements to return')
        self.assertEqual(unicore.first(None, 5), [], 'returns an empty array when called with an explicit number of elements to return')
        self.assertEqual(unicore.first([]), None, 'return undefined when called on a empty array')

    # def test_tail(self):
    #     self.assertEqual(unicore.tail, unicore.rest, 'is an alias for rest')

    # def test_drop(self):
    #     self.assertEqual(unicore.drop, unicore.rest, 'is an alias for rest')

    def test_initial(self):
        self.assertEqual(unicore.initial([1, 2, 3, 4, 5]), [1, 2, 3, 4], 'returns all but the last element')
        self.assertEqual(unicore.initial([1, 2, 3, 4], 2), [1, 2], 'returns all but the last n elements')
        self.assertEqual(unicore.initial([1, 2, 3, 4], 6), [], 'returns an empty array when n > length')
        result = (lambda: unicore.initial(1, 2, 3, 4))()
        self.assertEqual(result, [1, 2, 3], 'works on an arguments object')
        result = map(lambda x: unicore.initial(x), [[1, 2, 3], [1, 2, 3]])
        self.assertEqual(list(unicore.flatten(result)), [1, 2, 1, 2], 'works well with unicore.map')

    def test_last(self):
        self.assertEqual(unicore.last([1, 2, 3]), 3, 'can pull out the last element of an array')
        self.assertEqual(unicore.last([1, 2, 3]), 3, 'can perform OO-style "last()"')
        self.assertEqual(unicore.last([1, 2, 3], 0), [], 'returns an empty array when n <= 0 (0 case)')
        self.assertEqual(unicore.last([1, 2, 3], -1), [], 'returns an empty array when n <= 0 (negative case)')
        self.assertEqual(unicore.last([1, 2, 3], 2), [2, 3], 'can fetch the last n elements')
        self.assertEqual(unicore.last([1, 2, 3], 5), [1, 2, 3], 'returns the whole array if n > length')
        # result = (lambda: unicore.last(1, 2, 3, 4))()
        # self.assertEqual(result, 4, 'works on an arguments object')
        # result = map(lambda x: unicore.last(x), [[1, 2, 3], [], [1, 2, 3]])
        # self.assertEqual(list(result), [3, None, 3], 'works well with _.map')
        self.assertEqual(unicore.last(None), None, 'returns undefined when called on null')
        self.assertEqual(unicore.last([], 10), [], 'returns an empty array when called with an explicit number of elements to return')
        self.assertEqual(unicore.last([], 1), [], 'returns an empty array when called with an explicit number of elements to return')
        self.assertEqual(unicore.last(None, 5), [], 'returns an empty array when called with an explicit number of elements to return')
        self.assertEqual(unicore.last([]), None, 'return undefined when called on a empty array')

    def test_map(self):
        result = unicore.map([1, 2, 3], lambda x: x * 2)
        self.assertEqual(result, [2, 4, 6])

    def test_filter(self):
        result = unicore.filter([1, 2, 3, 4], lambda x: x % 2 == 0)
        self.assertEqual(result, [2, 4])

    def test_reduce(self):
        result = unicore.reduce([1, 2, 3, 4], lambda acc, x: acc + x, 0)
        self.assertEqual(result, 10)

    def test_find(self):
        result = unicore.find([1, 2, 3, 4], lambda x: x > 2)
        self.assertEqual(result, 3)

    def test_uniq(self):
        result = unicore.uniq([1, 2, 2, 3, 4, 4])
        self.assertEqual(result, [1, 2, 3, 4])

    def test_flatten(self):
        result = unicore.flatten([1, [2, [3, 4]], 5], 2)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_chunk(self):
        result = unicore.chunk([1, 2, 3, 4, 5], 2)
        self.assertEqual(result, [[1, 2], [3, 4], [5]])

    def test_initial(self):
        result = unicore.initial([1, 2, 3, 4], 2)
        self.assertEqual(result, [1, 2])

    def test_rest(self):
        result = unicore.rest([1, 2, 3, 4], 2)
        self.assertEqual(result, [3, 4])

    def test_contains(self):
        self.assertTrue(unicore.contains([1, 2, 3], 2))
        self.assertFalse(unicore.contains([1, 2, 3], 4))

    def test_range(self):
        self.assertEqual(unicore.range(5), [0, 1, 2, 3, 4])
        self.assertEqual(unicore.range(1, 5), [1, 2, 3, 4])
        self.assertEqual(unicore.range(1, 10, 2), [1, 3, 5, 7, 9])

    def test_difference(self):
        result = unicore.difference([1, 2, 3, 4], [2, 4])
        self.assertEqual(result, [1, 3])

    def test_intersection(self):
        result = unicore.intersection([1, 2, 3], [2, 3, 4])
        self.assertEqual(result, [2, 3])

    def test_union(self):
        result = unicore.union([1, 2], [2, 3])
        self.assertEqual(result, [1, 2, 3])

    def test_shuffle(self):
        array = [1, 2, 3, 4, 5]
        shuffled = unicore.shuffle(array)
        self.assertCountEqual(shuffled, array)  # Same elements, different order

    def test_pluck(self):
        result = unicore.pluck([{"a": 1}, {"a": 2}], "a")
        self.assertEqual(result, [1, 2])

    def test_sample(self):
        array = [1, 2, 3, 4, 5]
        sample = unicore.sample(array, 2)
        self.assertEqual(len(sample), 2)
        for item in sample:
            self.assertIn(item, array)

    # ------- Object Functions ------- #

    def test_keys(self):
        result = unicore.keys({"a": 1, "b": 2})
        self.assertEqual(result, ["a", "b"])

    def test_values(self):
        result = unicore.values({"a": 1, "b": 2})
        self.assertEqual(result, [1, 2])

    def test_defaults(self):
        obj = {"a": 1}
        unicore.defaults(obj, {"a": 0, "b": 2})
        self.assertEqual(obj, {"a": 1, "b": 2})

    def test_mapObject(self):
        result = unicore.mapObject({"a": 1, "b": 2}, lambda x: x * 2)
        self.assertEqual(result, {"a": 2, "b": 4})

    def test_matches(self):
        matcher = unicore.matches({"a": 1})
        self.assertTrue(matcher({"a": 1, "b": 2}))
        self.assertFalse(matcher({"a": 2, "b": 2}))

    def test_size(self):
        self.assertEqual(unicore.size([1, 2, 3]), 3)
        self.assertEqual(unicore.size({"a": 1, "b": 2}), 2)

    def test_toArray(self):
        self.assertEqual(unicore.toArray((1, 2, 3)), [1, 2, 3])
        self.assertEqual(unicore.toArray({"a": 1, "b": 2}), [1, 2])

    def test_where(self):
        result = unicore.where([{"a": 1}, {"a": 2}, {"a": 1}], {"a": 1})
        self.assertEqual(result, [{"a": 1}, {"a": 1}])

    # ------- Type Checking Functions ------- #

    def test_isString(self):
        self.assertTrue(unicore.isString("hello"))
        self.assertFalse(unicore.isString(123))

    def test_isArray(self):
        self.assertTrue(unicore.isArray([1, 2, 3]))
        self.assertFalse(unicore.isArray("hello"))

    def test_isEmpty(self):
        self.assertTrue(unicore.isEmpty([]))
        self.assertTrue(unicore.isEmpty({}))
        self.assertFalse(unicore.isEmpty([1, 2]))

    def test_isMatch(self):
        self.assertTrue(unicore.isMatch({"a": 1, "b": 2}, {"a": 1}))
        self.assertFalse(unicore.isMatch({"a": 1, "b": 2}, {"a": 2}))

    # ------- Functional Utilities ------- #

    def test_once(self):
        func = unicore.once(lambda: "called")
        result = func()
        self.assertEqual(result, "called")
        self.assertIsNone(func())

    def test_memoize(self):
        def factorial(n):
            return n * factorial(n - 1) if n > 1 else 1
        memoized_factorial = unicore.memoize(factorial)
        self.assertEqual(memoized_factorial(5), 120)
        self.assertEqual(memoized_factorial(5), 120)  # Should hit the cache

    def test_bindAll(self):
        class MyClass:
            def __init__(self, value):
                self.value = value

            def get_value(self):
                return self.value

        obj = MyClass(10)
        unicore.bindAll(obj, "get_value")
        self.assertEqual(obj.get_value(), 10)

    def test_defer(self):
        output = []
        def append_to_output():
            output.append("deferred")
        
        unicore.defer(append_to_output)
        # Give a small delay to allow defer to execute in background
        import time; time.sleep(0.1)
        self.assertEqual(output, ["deferred"])

    # ------- Helpers and Miscellaneous ------- #

    def test_random(self):
        result = unicore.random(1, 10)
        self.assertTrue(1 <= result <= 10)

    def test_constant(self):
        const_func = unicore.constant(42)
        self.assertEqual(const_func(), 42)

    def test_wrap(self):
        def greet(name):
            return f"Hello, {name}!"
        wrapped_greet = unicore.wrap(greet, lambda f, name: f(name).upper())
        self.assertEqual(wrapped_greet("world"), "HELLO, WORLD!")

    def test_chain(self):
        result = unicore.chain([1, 2, 3]).map(lambda x: x * 2).filter(lambda x: x > 2).value()
        self.assertEqual(result, [4, 6])

if __name__ == "__main__":
    unittest.main()