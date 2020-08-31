from functools import reduce
import itertools

class Enumerable:
    def __init__(self, iterable):
        self._iterable = iterable

    def __iter__(self):
        return self._iterable.__iter__()

    def filter(self, func, *args, **kwargs):
        return Enumerable((x for x in self._iterable if func(x, *args, **kwargs)))

    def map(self, func, *args, **kwargs):
        return Enumerable((func(x, *args, **kwargs) for x in self._iterable))

    def reduce(self, func, initializer=0, *args, **kwargs):
        def reduce_func(accumulator, value):
            return func(accumulator, value, *args, **kwargs)

        return reduce(reduce_func, self._iterable, initializer)

    def compact(self):
        return Enumerable((x for x in self._iterable if x is not None))

    def group_by(self, func, *args, **kwargs):
        """
        Group the values of the enumerable by func(val, *args, **kwargs)

        Results in pairs:
            (return value of func, list of all values evaluating to that return value)

        Example:
            ...
        """
        ...
        # how to do this as a generator?
        # sort and then groupby (both as generators)

    def index_by(self, func, *args, **kwargs):
        """
        Index the value by the result of func(val, *args, **kwargs):

        Assumes only a single value will evaluate to the same func return value.
        """
        return ((func(x, *args, **kwargs), x) for x in self._iterable)

    def all_combinations(self):
        pass

    def each_cons(self, n, inner=tuple):
        """
        Creates a sliding window across the iterable

        Example:
            Enumerable([1, 2, 3, 4]).each_cons(2).to(list)
                # -> [(1, 2), (

        """
        return Enumerable(
        )

    def _each_cons_generator(self, n, inner):
        current_cons = []
        for item in iterable:
            current_slice.append(item)
            if len(current_slice) >= size:
                yield current_slice
                current_slice = []
        if current_slice:
            yield current_slice

    def each_slice(self, n, inner=tuple):
        """
        Slices the iterable into lists of size n

        Will return a small trailing slice if not enough values.

        Example:
            Enumerable([1, 2, 3, 4, 5, 6, 7]).each_slice(3).to(list)
                # -> [[1, 2, 3], [4, 5, 6], [7]]
        """
        return Enumerable(self._each_slice_generator(n))

    def _each_slice_generator(self, n):
        current_slice = []
        for item in iterable:
            current_slice.append(item)
            if len(current_slice) >= size:
                yield current_slice
                current_slice = []
        if current_slice:
            yield current_slice

    def to(self, container_type):
        return container_type(self._iterable)


def Filter(iterable, func, *args, **kwargs):
    return Enumerable(iterable).filter(func, *args, **kwargs)


def Map(iterable, func, *args, **kwargs):
    return Enumerable(iterable).map(func, *args, **kwargs)


def Reduce(iterable, func, initializer=0, *args, **kwargs):
    return Enumerable(iterable).reduce(func, initializer, *args, **kwargs)
