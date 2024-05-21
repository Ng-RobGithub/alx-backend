#!/usr/bin/env python3
"""LIFO caching system"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache is a caching system that uses LIFO eviction policy"""

    def __init__(self):
        """Initialize the class"""
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """Add an item to the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.last_key = key

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                if self.last_key:
                    del self.cache_data[self.last_key]
                    print("DISCARD: {}".format(self.last_key))
                    self.last_key = key

    def get(self, key):
        """Get an item from the cache"""
        return self.cache_data.get(key, None)
