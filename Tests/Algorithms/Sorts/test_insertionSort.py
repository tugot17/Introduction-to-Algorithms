from unittest import TestCase

from Algorithms.Sorts.InsertionSort import InsertionSort
from Tests.Algorithms.Sorts.test_sort_helper import test_sort_helper_1, test_sort_helper_2, \
    test_sort_sorted_array_helper


class TestInsertionSort(TestCase):
    def test_insertion_sort1(self):
        insert_sort = InsertionSort()
        test_sort_helper_1(insert_sort)

    def test_insertion_sort2(self):
        insert_sort = InsertionSort()
        test_sort_helper_2(insert_sort)

    def test_sorted_array_sort(self):
        insert_sort = InsertionSort()
        test_sort_sorted_array_helper(insert_sort)