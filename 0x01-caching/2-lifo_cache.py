#!/usr/bin/env python3
"""LIFO caching system"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache is a caching system that uses LIFO eviction policy"""

    def __init__(self):
        """Initialize the class"""
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """Add an item to the cache"""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.stack.remove(key)
            self.cache_data[key] = item
            self.stack.append(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last_key = self.stack.pop()
                del self.cache_data[last_key]
                print("DISCARD: {}".format(last_key))

    def get(self, key):
        """Get an item from the cache"""
        return self.cache_data.get(key, None)
