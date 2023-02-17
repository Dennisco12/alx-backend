#!/usr/bin/env python3
"""This returns a tuple of size two"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """This returns a tuple containing a start index and an end
    index corresponding to the range of indexes to return in a
    list for those particular pagination parameter"""
    tup = []
    start_index = (page - 1) * page_size
    end_index = page * page_size
    tup.append(start_index)
    tup.append(end_index)
    return tuple(tup)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """This returns the data in a particular page"""
        if not isinstance(page, int):
            raise AssertionError
        if not isinstance(page_size, int):
            raise AssertionError
        if page <= 0 or page_size <= 0:
            raise AssertionError
        location = index_range(page, page_size)
        try:
            self.dataset()
            return self.__dataset[location[0]: location[1]]
        except IndexError:
            return []
