#!/usr/bin/python3
""" MRU caching """

from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """ MRU cache class """

    def __init__(self):
        """ Initialize MRU cache """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                and key not in self.cache_data:
            last_used_key = next(reversed(self.cache_data))
            del self.cache_data[last_used_key]
            print("DISCARD:", last_used_key)

        self.cache_data[key] = item

    def get(self, key):
        """ Retrieve an item from cache """
        if key is None or key not in self.cache_data:
            return None

        value = self.cache_data.pop(key)
        self.cache_data[key] = value
        return value

    def print_cache(self):
        """ Print cache content """
        print("Current cache:")
        for key, value in self.cache_data.items():
            print("{}: {}".format(key, value))
