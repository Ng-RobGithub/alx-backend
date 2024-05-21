#!/usr/bin/env python3
"""FIFO caching system"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache is a caching system that uses FIFO eviction policy"""

    def __init__(self):
        """Initialize the class"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item to the cache"""
        if key is not None and item is not None:
            if key not in self.cache_data:
                self.order.append(key)
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key = self.order.pop(0)
                del self.cache_data[first_key]
                print("DISCARD: {}".format(first_key))

    def get(self, key):
        """Get an item from the cache"""
        return self.cache_data.get(key, None)
