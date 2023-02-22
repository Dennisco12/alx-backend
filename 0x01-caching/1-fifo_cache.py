#!/usr/bin/env python3
"""This is a caching system which uses the fifo policy"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """This defines the cache"""
    def __init__(self):
        """This initializes the class"""
        super().__init__()
        self.addOrder = []

    def put(self, key, item):
        """This adds an item to the cache dict"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        self.addOrder.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print('DISCARD: ' + self.addOrder[0])
            del self.cache_data[self.addOrder[0]]
            del self.addOrder[0]

    def get(self, key):
        """This retrieves an item from the cache dict"""
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data.get(key)
