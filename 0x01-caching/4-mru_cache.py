#!/usr/bin/env python3
"""This is the Most Recently Used caching system"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """This defines the caching class"""
    def __init__(self):
        """This initializes the class"""
        super().__init__()
        self.useOrder = []

    def put(self, key, item):
        """This adds an item to the cache dict"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            print("DISCARD: " + self.useOrder[-1])
            del self.cache_data[self.useOrder[-1]]
            del self.useOrder[-1]

        if key not in self.useOrder:
            self.useOrder.append(key)

    def get(self, key):
        """This retrieves an item from the cache dict"""
        if key is None or key not in self.cache_data:
            return None
        if key in self.useOrder:
            self.useOrder.remove(key)
            self.useOrder.append(key)

        return self.cache_data[key]
