#!/usr/bin/env python3
"""Last-In First-Out caching module.
"""
from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dictionary with a LIFO
    removal mechanism when the limit is reached.
    """

    def __init__(self):
        """Initializes the cache.

        Uses an OrderedDict to maintain the order of insertion.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache.

        If the cache exceeds the maximum size, it discards
        the last added item according to the LIFO policy.

        Args:
            key (str): The key under which the item is stored.
            item (any): The item to store in the cache.
        """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(last=True)
                print("DISCARD:", last_key)

        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Retrieves an item by key.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            The item stored under the given key, or None if the key
            does not exist.
        """
        return self.cache_data.get(key, None)
