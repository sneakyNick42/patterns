"""Facade pattern module."""
import time
import random
from typing import List

ARRAY = random.sample(range(100000), 100000)


def timer(func):
    """Timer decorator."""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('Sorting using {0} took {1} seconds'.format(result, end - start))

    return wrapper


class SortA:
    """Class for sorting a list with .sort()."""
    @staticmethod
    @timer
    def sort(array: List[int]) -> str:
        """
        Sort a list of integers using .sort().

        :param array: List of integers
        :return: Sorting function name
        :rtype: str
        """
        array.sort()
        return '.sort()'


class SortB:
    """Class for sorting a list with sorted()."""
    @staticmethod
    @timer
    def sort(array: List[int]) -> str:
        """
        Sort a list of integers using sorted().

        :param array: List of integers
        :return: Sorting function name
        :rtype: str
        """
        sorted(array)
        return 'sorted()'


class SortingTimeFacade:
    """Facade class for sorting classes."""
    def __init__(self) -> None:
        self._sort_a = SortA()
        self._sort_b = SortB()

    def sort(self, array):
        """Calling sorting classes methods."""
        self._sort_a.sort(array)
        self._sort_b.sort(array)


if __name__ == '__main__':
    SORTING_FACADE = SortingTimeFacade()
    SORTING_FACADE.sort(ARRAY)
