#!/usr/bin/python3
""" MRU Cache Module """
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ MRU Cache class """

    def __init__(self):
        """ Initialize MRU Cache """
        super().__init__()

    def put(self, key, item):
        """ Add an item to the cache """
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

        # Move the accessed item to the end of the cache_data
        item = self.cache_data.pop(key)
        self.cache_data[key] = item

        return item

    def print_cache(self):
        """ Print the cache """
        print("Current cache:")
        for k, v in self.cache_data.items():
            print("{}: {}".format(k, v))
