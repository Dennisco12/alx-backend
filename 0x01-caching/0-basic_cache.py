#!/usr/bin/env python3
"""This is a caching system"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """This defines the caching class"""
    def __init__(self):
        """this initializes the class"""
        super().__init__()

    def put(self, key, item):
        """This adds an input to the cache dictionary"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """This return the value of an item from the cache dict"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
