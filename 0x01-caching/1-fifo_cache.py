#!/usr/bin/env python3
"""A script for FIFO caching system
"""


BaseCaching = __import__('base_caching').BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """FIFO cache system"""

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()
    
    def put(self, key, item):
        """ put key value pair into cache"""
        if (not key or not item):
            return
        capacity = BaseCaching.MAX_ITEMS
        discarded = None

        if key not in self.cache_data:
            self.cache_data[key] = item
        if len(self.cache_data) > capacity:
            discarded = self.cache_data.popitem(last=False)
        print(f"DISCARD: {discarded}\n")
        
        
        
    def get(self, key):
        """ return the value in self.cache_data linked to key."""
        
        if (key is None or key not in self.cache_data):
            return none
        return self.cache_data.get(key)