#!/usr/bin/env python3
"""Least Recently Used caching module.
"""
from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dictionary with an LRU
    removal mechanism when the limit is reached.
    """

    def __init__(self):
        """Initializes the cache.

        Uses an OrderedDict to maintain the order of access.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache.

        If the cache exceeds the maximum size, it discards
        the least recently used item according to the LRU policy.

        Args:
            key (str): The key under which the item is stored.
            item (any): The item to store in the cache.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            """ Move the key to the end to show it was recently used """
            self.cache_data.move_to_end(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            """ Pop the first item (least recently used) """
            oldest_key, _ = self.cache_data.popitem(last=False)
            print("DISCARD:", oldest_key)

        self.cache_data[key] = item
        self.cache_data.move_to_end(key)

    def get(self, key):
        """Retrieves an item by key.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            The item stored under the given key, or None if the key
            does not exist.
        """
        if key is not None and key in self.cache_data:
            """ Move the key to the end to show it was recently used """
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
