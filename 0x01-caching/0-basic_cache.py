#!/usr/bin/env python3
"""Basic caching system"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache is a basic caching system with no limits"""

    def put(self, key, item):
        """Add an item to the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item from the cache"""
        return self.cache_data.get(key, None)
