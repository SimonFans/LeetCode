Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

# Method 

from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.hashMap = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.hashMap:
            self.hashMap.move_to_end(key)
            return self.hashMap[key]
        return -1

    def put(self, key: int, value: int) -> None:
        # if key exists, then update so have to move to the end first
        if key in self.hashMap:
            self.hashMap.move_to_end(key)
        # new key:value or update existing key with new value
        self.hashMap[key] = value
        if len(self.hashMap) > self.capacity:
            self.hashMap.popitem(last=False)
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)



'''
OrderedDict 用法：
from collections import OrderedDict
h = OrderedDict()
h[2] = 2
h[1] = 1
h[3] = 3
print('Before moving:', h)
h.move_to_end(2)
print('After moving:', h)
# By default, LIFO h.popitem(last=True), you can change: FIFO h.popitem(last=False)
h.popitem()
print('Remove the last item', h)
h.popitem(last=False)
print('Remove the first item', h)

Before moving: OrderedDict([(2, 2), (1, 1), (3, 3)])
After moving: OrderedDict([(1, 1), (3, 3), (2, 2)])
Remove the last item OrderedDict([(1, 1), (3, 3)])
Remove the first item OrderedDict([(3, 3)])

'''
