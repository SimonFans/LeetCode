Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4


def __init__(self, capacity):
    """
    :type capacity: int
    """
    self.capacity = capacity
    self.cache = {} # 存放存入的键值对
    self.frequency = {} # 存放每个频率中出现的key，如{1：[key1,key2], 2:[key3]}
    self.cache_index = {} # 存放key对应的频率， 如{key1:1, key2:1, key3:2}

def get(self, key):
    """
    :type key: int
    :rtype: int
    """
    if key not in self.cache:
        return -1
    index = self.cache_index[key]
    self.frequency[index].remove(key)
    if self.frequency[index] == []:
        del self.frequency[index]
    if index+1 in self.frequency:
        self.frequency[index+1].append(key)
    else:
        self.frequency[index+1] = [key]
    self.cache_index[key] += 1
    return self.cache[key]
    


def put(self, key, value):
    """
    :type key: int
    :type value: int
    :rtype: void
    """
    if self.capacity <= 0:
        return 
    if key in self.cache:
        # 如果put一个已经存在的key,修改它的value和frequency
        self.cache[key] = value
        self.get(key)
        return
    if len(self.cache) == self.capacity:
        for times in self.frequency: # 因为字典有序，所以第一个肯定是频率最小的，删除后通过break退出循环
            key_of_cache = self.frequency[times][0] # 取出频率最小的key，并删除
            del self.cache[key_of_cache]
            del self.cache_index[key_of_cache]
            self.frequency[times] = self.frequency[times][1:]
            if self.frequency[times] == []:
                del self.frequency[times]
                break
    # 插入一个新值,频率初始值为1
    self.cache[key] = value
    if 1 in self.frequency:
        self.frequency[1].append(key)
    else:
        self.frequency[1] = [key]
    self.cache_index[key] = 1
