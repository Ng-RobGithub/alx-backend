#!/usr/bin/python3
""" Least Frequently Used caching module """
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """ LFU caching system """

    def __init__(self):
        """ Initialize class instance. """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.cache_data.move_to_end(key)
            else:
                # Discard the least frequently used item
                discarded_key, _ = self.cache_data.popitem(last=False)
                print("DISCARD:", discarded_key)
                self.cache_data[key] = item
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
