import sys
import os
import unittest

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from unicore import unicore  # Now you can import unicore as usual

class TestArrays(unittest.TestCase):

    def test_first(self):
        self.assertEqual(unicore.first([1, 2, 3]), 1, 'can pull out the first element of an array')
        self.assertEqual(unicore.first([1, 2, 3]), 1, 'can perform OO-style "first()"')
        self.assertEqual(unicore.first([1, 2, 3], 0), [], 'returns an empty array when n <= 0 (0 case)')
        self.assertEqual(unicore.first([1, 2, 3], -1), [], 'returns an empty array when n <= 0 (negative case)')
        self.assertEqual(unicore.first([1, 2, 3], 2), [1, 2], 'can fetch the first n elements')
        self.assertEqual(unicore.first([1, 2, 3], 5), [1, 2, 3], 'returns the whole array if n > length')
        result = (lambda: unicore.first(4, 3, 2, 1))()
        self.assertEqual(result, 4, 'works on an arguments object')
        result = map(lambda x: unicore.first(x), [[1, 2, 3], [], [1, 2, 3]])
        self.assertEqual(list(result), [1, None, 1], 'works well with _.map')
        self.assertEqual(unicore.first(None), None, 'returns undefined when called on null')
        self.assertEqual(unicore.first([], 10), [], 'returns an empty array when called with an explicit number of elements to return')
        self.assertEqual(unicore.first([], 1), [], 'returns an empty array when called with an explicit number of elements to return')
        self.assertEqual(unicore.first(None, 5), [], 'returns an empty array when called with an explicit number of elements to return')
        self.assertEqual(unicore.first([]), None, 'return undefined when called on a empty array')


    def test_head(self):
        self.assertEqual(head, first, 'is an alias for first')

    def test_take(self):
        self.assertEqual(take, first, 'is an alias for first')

    def test_rest(self):
        numbers = [1, 2, 3, 4]
        self.assertEqual(rest(numbers), [2, 3, 4], 'fetches all but the first element')
        self.assertEqual(rest(numbers, 0), [1, 2, 3, 4], 'returns the whole array when index is 0')
        self.assertEqual(rest(numbers, 2), [3, 4], 'returns elements starting at the given index')
        result = (lambda: rest(1, 2, 3, 4))()
        self.assertEqual(result, [2, 3, 4], 'works on an arguments object')
        result = map(lambda x: rest(x), [[1, 2, 3], [1, 2, 3]])
        self.assertEqual(list(flatten(result)), [2, 3, 2, 3], 'works well with _.map')

    def test_tail(self):
        self.assertEqual(tail, rest, 'is an alias for rest')

    def test_drop(self):
        self.assertEqual(drop, rest, 'is an alias for rest')

    def test_initial(self):
        self.assertEqual(initial([1, 2, 3, 4, 5]), [1, 2, 3, 4], 'returns all but the last element')
        self.assertEqual(initial([1, 2, 3, 4], 2), [1, 2], 'returns all but the last n elements')
        self.assertEqual(initial([1, 2, 3, 4], 6), [], 'returns an empty array when n > length')
        result = (lambda: initial(1, 2, 3, 4))()
        self.assertEqual(result, [1, 2, 3], 'works on an arguments object')
        result = map(lambda x: initial(x), [[1, 2, 3], [1, 2, 3]])
        self.assertEqual(list(flatten(result)), [1, 2, 1, 2], 'works well with _.map')

    def test_last(self):
        self.assertEqual(last([1, 2, 3]), 3, 'can pull out the last element of an array')
        self.assertEqual(last([1, 2, 3]), 3, 'can perform OO-style "last()"')
        self.assertEqual(last([1, 2, 3], 0), [], 'returns an empty array when n <= 0 (0 case)')
        self.assertEqual(last([1, 2, 3], -1), [], 'returns an empty array when n <= 0 (negative case)')
        self.assertEqual(last([1, 2, 3], 2), [2, 3], 'can fetch the last n elements')
        self.assertEqual(last([1, 2, 3], 5), [1, 2, 3], 'returns the whole array if n > length')
        result = (lambda: last(1, 2, 3, 4))()
        self.assertEqual(result, 4, 'works on an arguments object')
        result = map(lambda x: last(x), [[1, 2, 3], [], [1, 2, 3]])
        self.assertEqual(list(result), [3, None, 3], 'works well with _.map')
        self.assertEqual(last(None), None, 'returns undefined when called on null')
        self.assertEqual(last([], 10), [], 'returns an empty array when called with an explicit number of elements to return')
        self.assertEqual(last([], 1), [], 'returns an empty array when called with an explicit number of elements to return')
        self.assertEqual(last(None, 5), [], 'returns an empty array when called with an explicit number of elements to return')

        arr = []
        arr[-1] = 'boo'
        self.assertEqual(last(arr), None, 'return undefined when called on a empty array')

    def test_compact(self):
        self.assertEqual(compact([1, False, None, 0, '', None, float('nan'), 2]), [1, 2], 'removes all falsy values')
        result = (lambda: compact(0, 1, False, 2, False, 3))()
        self.assertEqual(result, [1, 2, 3], 'works on an arguments object')
        result = map(lambda x: compact(x), [[1, False, False], [False, False, 3]])
        self.assertEqual(list(result), [[1], [3]], 'works well with _.map')

    def test_flatten(self):
        self.assertEqual(flatten(None), [], 'supports null')
        self.assertEqual(flatten(None), [], 'supports undefined')

        self.assertEqual(flatten([[], [[]], []]), [], 'supports empty arrays')
        self.assertEqual(flatten([[], [[]], []], True), [[]], 'can shallowly flatten empty arrays')

        list_ = [1, [2], [3, [[[4]]]]]
        self.assertEqual(flatten(list_), [1, 2, 3, 4], 'can flatten nested arrays')
        self.assertEqual(flatten(list_, True), [1, 2, 3, [[[4]]]], 'can shallowly flatten nested arrays')
        self.assertEqual(flatten(list_, False), [1, 2, 3, 4], 'false means deep')
        result = (lambda: flatten(1, [2], [3, [[[4]]]]))()
        self.assertEqual(result, [1, 2, 3, 4], 'works on an arguments object')
        list_ = [[1], [2], [3], [[4]]]
        self.assertEqual(flatten(list_, True), [1, 2, 3, [4]], 'can shallowly flatten arrays containing only other arrays')
        list_ = [1, [2], [[3]], [[[4]]]]
        self.assertEqual(flatten(list_, 2), [1, 2, 3, [4]], 'can flatten arrays to a given depth')
        self.assertEqual(flatten(list_, 0), list_, 'can flatten arrays to depth of 0')
        self.assertEqual(flatten(list_, -1), list_, 'can flatten arrays to depth of -1')

        self.assertEqual(len(flatten([range(10), range(10), 5, 1, 3], True)), 23, 'can flatten medium length arrays')
        self.assertEqual(len(flatten([range(10), range(10), 5, 1, 3])), 23, 'can shallowly flatten medium length arrays')
        self.assertEqual(len(flatten([[None] * 1000000, range(56000), 5, 1, 3])), 1056003, 'can handle massive arrays')
        self.assertEqual(len(flatten([[None] * 1000000, range(56000), 5, 1, 3], True)), 1056003, 'can handle massive arrays in shallow mode')

        x = range(100000)
        for i in range(1000):
            x = [x]
        self.assertEqual(flatten(x), range(100000), 'can handle very deep arrays')
        self.assertEqual(flatten(x, True), x[0], 'can handle very deep arrays in shallow mode')

    def test_without(self):
        list_ = [1, 2, 1, 0, 3, 1, 4]
        self.assertEqual(without(list_, 0, 1), [2, 3, 4], 'removes all instances of the given values')
        result = (lambda: without(1, 2, 1, 0, 3, 1, 4))()
        self.assertEqual(result, [2, 3, 4], 'works on an arguments object')

        list_ = [{'one': 1}, {'two': 2}]
        self.assertEqual(without(list_, {'one': 1}), list_, 'compares objects by reference (value case)')
        self.assertEqual(without(list_, list_[0]), [{'two': 2}], 'compares objects by reference (reference case)')

    def test_sortedIndex(self):
        numbers = [10, 20, 30, 30, 30, 40, 50, 60]
        indexFor35 = sortedIndex(numbers, 35)
        self.assertEqual(indexFor35, 5, 'finds the index at which a value should be inserted to retain order')
        indexFor30 = sortedIndex(numbers, 30)
        self.assertEqual(indexFor30, 2, 'finds the smallest index at which a value could be inserted to retain order')

        objects = [{'x': 10}, {'x': 20}, {'x': 30}, {'x': 40}]
        iterator = lambda obj: obj['x']
        self.assertEqual(sortedIndex(objects, {'x': 25}, iterator), 2, 'uses the result of `iterator` for order comparisons')
        self.assertEqual(sortedIndex(objects, {'x': 35}, 'x'), 3, 'when `iterator` is a string, uses that key for order comparisons')

        context = {1: 2, 2: 3, 3: 4}
        iterator = lambda obj: context[obj]
        self.assertEqual(sortedIndex([1, 3], 2, iterator, context), 1, 'can execute its iterator in the given context')

        values = [0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287,
                  1048575, 2097151, 4194303, 8388607, 16777215, 33554431, 67108863, 134217727, 268435455, 536870911, 1073741823, 2147483647]
        largeArray = [None] * (2**32 - 1)
        length = len(values)
        # Sparsely populate `array`
        while length:
            length -= 1
            largeArray[values[length]] = values[length]

        self.assertEqual(sortedIndex(largeArray, 2147483648), 2147483648, 'works with large indexes')

    def test_uniq(self):
        list_ = [1, 2, 1, 3, 1, 4]
        self.assertEqual(uniq(list_), [1, 2, 3, 4], 'can find the unique values of an unsorted array')
        list_ = [1, 1, 1, 2, 2, 3]
        self.assertEqual(uniq(list_, True), [1, 2, 3], 'can find the unique values of a sorted array faster')

        list_ = [-2, -1, 0, 1, 2]
        notInjective = lambda x: x * x
        self.assertEqual(uniq(list_, True, notInjective), [-2, -1, 0], 'can find values of sorted array which map to unique values through a non one-to-one function by switching to slower algorithm even when isSorted=true')

        list_ = [{'name': 'Moe'}, {'name': 'Curly'}, {'name': 'Larry'}, {'name': 'Curly'}]
        expected = [{'name': 'Moe'}, {'name': 'Curly'}, {'name': 'Larry'}]
        iterator = lambda stooge: stooge['name']
        self.assertEqual(uniq(list_, False, iterator), expected, 'uses the result of `iterator` for uniqueness comparisons (unsorted case)')
        self.assertEqual(uniq(list_, iterator), expected, '`sorted` argument defaults to false when omitted')
        self.assertEqual(uniq(list_, 'name'), expected, 'when `iterator` is a string, uses that key for comparisons (unsorted case)')

        list_ = [{'score': 8}, {'score': 10}, {'score': 10}]
        expected = [{'score': 8}, {'score': 10}]
        iterator = lambda item: item['score']
        self.assertEqual(uniq(list_, True, iterator), expected, 'uses the result of `iterator` for uniqueness comparisons (sorted case)')
        self.assertEqual(uniq(list_, True, 'score'), expected, 'when `iterator` is a string, uses that key for comparisons (sorted case)')

        self.assertEqual(uniq([{0: 1}, {0: 1}, {0: 1}, {0: 2}], 0), [{0: 1}, {0: 2}], 'can use falsy pluck like iterator')

        result = (lambda: uniq(1, 2, 1, 3, 1, 4))()
        self.assertEqual(result, [1, 2, 3, 4], 'works on an arguments object')

        a = {}, b = {}, c = {}
        self.assertEqual(uniq([a, b, a, b, c]), [a, b, c], 'works on values that can be tested for equivalency but not ordered')

        self.assertEqual(uniq(None), [], 'returns an empty array when `array` is not iterable')

        context = {}
        list_ = [3]
        uniq(list_, lambda value, index, array: (
            self.assertEqual(context, context, 'executes its iterator in the given context'),
            self.assertEqual(value, 3, 'passes its iterator the value'),
            self.assertEqual(index, 0, 'passes its iterator the index'),
            self.assertEqual(array, list_, 'passes its iterator the entire array')
        ), context)

    def test_unique(self):
        self.assertEqual(unique, uniq, 'is an alias for uniq')

    def test_intersection(self):
        stooges = ['moe', 'curly', 'larry']
        leaders = ['moe', 'groucho']
        self.assertEqual(intersection(stooges, leaders), ['moe'], 'can find the set intersection of two arrays')
        self.assertEqual(intersection(stooges, leaders), ['moe'], 'can perform an OO-style intersection')
        result = (lambda: intersection(arguments, leaders))('moe', 'curly', 'larry')
        self.assertEqual(result, ['moe'], 'works on an arguments object')
        theSixStooges = ['moe', 'moe', 'curly', 'curly', 'larry', 'larry']
        self.assertEqual(intersection(theSixStooges, leaders), ['moe'], 'returns a duplicate-free array')
        result = intersection([2, 4, 3, 1], [1, 2, 3])
        self.assertEqual(result, [2, 3, 1], 'preserves the order of the first array')
        result = intersection(None, [1, 2, 3])
        self.assertEqual(result, [], 'returns an empty array when passed null as the first argument')
        result = intersection([1, 2, 3], None)
        self.assertEqual(result, [], 'returns an empty array when passed null as an argument beyond the first')

    def test_union(self):
        result = union([1, 2, 3], [2, 30, 1], [1, 40])
        self.assertEqual(result, [1, 2, 3, 30, 40], 'can find the union of a list of arrays')

        result = union([1, 2, 3], [2, 30, 1], [1, 40, [1]])
        self.assertEqual(result, [1, 2, 3, 30, 40, [1]], 'can find the union of a list of nested arrays')

        result = union([10, 20], [1, 30, 10], [0, 40])
        self.assertEqual(result, [10, 20, 1, 30, 0, 40], 'orders values by their first encounter')

        result = (lambda: union(arguments, [2, 30, 1], [1, 40]))(1, 2, 3)
        self.assertEqual(result, [1, 2, 3, 30, 40], 'works on an arguments object')

        self.assertEqual(union([1, 2, 3], 4), [1, 2, 3], 'restricts the union to arrays only')

    def test_difference(self):
        result = difference([1, 2, 3], [2, 30, 40])
        self.assertEqual(result, [1, 3], 'can find the difference of two arrays')

        result = difference([1, 2, 3], [2, 30, 40, [1]])
        self.assertEqual(result, [1, 3], 'avoids deep flattening of arrays')

        result = difference([1, 2, 3, 4], [2, 30, 40], [1, 11, 111])
        self.assertEqual(result, [3, 4], 'can find the difference of three arrays')

        result = difference([8, 9, 3, 1], [3, 8])
        self.assertEqual(result, [9, 1], 'preserves the order of the first array')

        result = (lambda: difference(arguments, [2, 30, 40]))(1, 2, 3)
        self.assertEqual(result, [1, 3], 'works on an arguments object')

        result = difference([1, 2, 3], 1)
        self.assertEqual(result, [1, 2, 3], 'restrict the difference to arrays only')

    def test_zip(self):
        names = ['moe', 'larry', 'curly']
        ages = [30, 40, 50]
        leaders = [True]
        self.assertEqual(zip(names, ages, leaders), [
            ['moe', 30, True],
            ['larry', 40, None],
            ['curly', 50, None]
        ], 'zipped together arrays of different lengths')

        stooges = zip(['moe', 30, 'stooge 1'], ['larry', 40, 'stooge 2'], ['curly', 50, 'stooge 3'])
        self.assertEqual(stooges, [['moe', 'larry', 'curly'], [30, 40, 50], ['stooge 1', 'stooge 2', 'stooge 3']], 'zipped pairs')

        # In the case of different lengths of the tuples, undefined values
        # should be used as placeholder
        stooges = zip(['moe', 30], ['larry', 40], ['curly', 50, 'extra data'])
        self.assertEqual(stooges, [['moe', 'larry', 'curly'], [30, 40, 50], [None, None, 'extra data']], 'zipped pairs with empties')

        empty = zip([])
        self.assertEqual(empty, [], 'unzipped empty')

        self.assertEqual(zip(None), [], 'handles null')
        self.assertEqual(zip(), [], '_.zip() returns []')

    def test_unzip(self):
        self.assertEqual(unzip(None), [], 'handles null')

        self.assertEqual(unzip([['a', 'b'], [1, 2]]), [['a', 1], ['b', 2]])

        # complements zip
        zipped = zip(['fred', 'barney'], [30, 40], [True, False])
        self.assertEqual(unzip(zipped), [['fred', 'barney'], [30, 40], [True, False]])

        zipped = zip(['moe', 30], ['larry', 40], ['curly', 50, 'extra data'])
        self.assertEqual(unzip(zipped), [['moe', 30, None], ['larry', 40, None], ['curly', 50, 'extra data']], 'Uses length of largest array')

    def test_object(self):
        result = object(['moe', 'larry', 'curly'], [30, 40, 50])
        shouldBe = {'moe': 30, 'larry': 40, 'curly': 50}
        self.assertEqual(result, shouldBe, 'two arrays zipped together into an object')

        result = object([['one', 1], ['two', 2], ['three', 3]])
        shouldBe = {'one': 1, 'two': 2, 'three': 3}
        self.assertEqual(result, shouldBe, 'an array of pairs zipped together into an object')

        stooges = {'moe': 30, 'larry': 40, 'curly': 50}
        self.assertEqual(object(pairs(stooges)), stooges, 'an object converted to pairs and back to an object')

        self.assertEqual(object(None), {}, 'handles nulls')

if __name__ == '__main__':
    unittest.main()

