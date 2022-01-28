#from collections import OrderedDict
from collections import defaultdict
import heapq
import random

class DataSource:
    def getRank(self):
        return random.randint(1,10)
    
class BestRetainCache:
    def __init__(self, capacity, ds):
        # Assume maximum capacity is 2
        self.capacity = capacity
        # Data Source {'A': 'aaa', 'B':'bbb', 'C':'ccc', 'D':'ddd', 'E': 'eee', 'F': 'fff'}
        self.ds = ds
        # Cache {k:v} where k is data, v is rank {'A': 'aaa'}
        self.cache = {}
        # just like {1:('A','D'), 2:('B','F')}
        self.rank = defaultdict(set)
        # [(rank_val, message_key),()...]
        self.minHeap = []
        
    def getKey(self, key):
        message = None
        # key exists in the current cache
        if key in self.cache:
            message = self.cache[key]
        # if key not exist in the current cache, then pull from data source
        else:
            message = self.ds[key]
            # First time to get Rank
            curRank = DataSource().getRank()
            # Add key to the Cache
            self.cache[key] = message
            # add new /update rank dictionary with keys in a set
            if curRank not in self.rank:
                self.rank[curRank].add(key)
            # append to the minHeap
            heapq.heappush(self.minHeap, (curRank, key))
            
            if len(self.cache) > self.capacity:
                lowest_rank, rm_key = self.removeLowestRank()
                del self.cache[rm_key]
                self.rank[lowest_rank].remove(rm_key)
                if len(self.rank[lowest_rank])== 0:
                    del self.rank[lowest_rank]
        print('cache:', self.cache)
        print('rank:', self.rank)
        print('minHeap', self.minHeap)
        return message  
                
    def removeLowestRank(self):
        lowest_rank, key = heapq.heappop(self.minHeap)
        return lowest_rank, key
            
            
obj = BestRetainCache(2, {'A': 'aaa', 'B':'bbb', 'C':'ccc', 'D':'ddd', 'E': 'eee', 'F': 'fff'})
print(obj.getKey('A'))
print('\n')
print(obj.getKey('B'))
print('\n')
print(obj.getKey('C'))

