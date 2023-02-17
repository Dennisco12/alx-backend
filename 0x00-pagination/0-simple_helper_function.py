#!/usr/bin/env python3
"""This returns a tuple of size two"""


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
