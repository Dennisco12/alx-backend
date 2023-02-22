#!/usr/bin/env python3
"""This is a LIF caching system"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """This defines the class"""
    def __init__(self):
        """This initializes the class"""
        super().__init__()
        self.addOrder = []

    def put(self, key, item):
        """This adds an item to the cache dict"""
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > self.MAX_ITEMS:
            print("DISCARD: " + self.addOrder[-1])
            del self.cache_data[self.addOrder[-1]]
            del self.addOrder[-1]

        self.addOrder.append(key)

    def get(self, key):
        """This retreves an item from storage"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
