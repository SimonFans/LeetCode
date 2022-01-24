'''
Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.

Implement the AllOne class:

AllOne() Initializes the object of the data structure.
inc(String key) Increments the count of the string key by 1. If key does not exist in the data structure, insert it with count 1.
dec(String key) Decrements the count of the string key by 1. If the count of key is 0 after the decrement, remove it from the data structure. It is guaranteed that key exists in the data structure before the decrement.
getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".

'''

Input
["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
[[], ["hello"], ["hello"], [], [], ["leet"], [], []]
Output
[null, null, null, "hello", "hello", null, "hello", "leet"]

Explanation
AllOne allOne = new AllOne();
allOne.inc("hello");
allOne.inc("hello");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "hello"
allOne.inc("leet");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "leet"


class AllOne:
    def __init__(self):
        # {'Hello':1, 'Leetcode':2}
        self.key_count = defaultdict(int)
        # {number: set()} => {1: ('Hello'), 2: ('Leetcode')}
        self.count_key = defaultdict(set)
        # Max heap => [-2,-1] remember using maxHeap, multiply by -1
        self.maxHeap = []
        # Min heap => [1,2]
        self.minHeap = []
        
    def inc(self, key: str) -> None:
        curr_cnt = self.key_count[key]
        if self.count_key[curr_cnt]:
            self.count_key[curr_cnt].remove(key)
        curr_cnt += 1 
        self.key_count[key] = curr_cnt
        self.count_key[curr_cnt].add(key)
        heapq.heappush(self.maxHeap,-curr_cnt)
        heapq.heappush(self.minHeap, curr_cnt)
        # print('-----')
        # print(self.key_count)
        # print(self.count_key)
        # print('maxHeap', self.maxHeap)
        # print('minHeap', self.minHeap)
            
    def dec(self, key: str) -> None:
        curr_cnt = self.key_count[key]
        self.count_key[curr_cnt].remove(key)
        curr_cnt -= 1
        if curr_cnt == 0:
            del self.key_count[key]
            return 
        self.key_count[key] =curr_cnt
        self.count_key[curr_cnt].add(key)
        heapq.heappush(self.maxHeap,-curr_cnt)
        heapq.heappush(self.minHeap, curr_cnt)
        # print(self.key_count)
        # print(self.count_key)
        
    def getMaxKey(self) -> str:
        if len(self.key_count) == 0:
            return ""
        while self.maxHeap:
            val = -heapq.heappop(self.maxHeap)
            if self.count_key[val]:
                # 还要放回去，不然接下来再call就会出错
                heapq.heappush(self.maxHeap, -val)
                for key in self.count_key[val]:
                    return key
        
    def getMinKey(self) -> str:
        if len(self.key_count) == 0:
            return ""
        
        # We will keep popping values from the min heap and if the values exits in 
        # the count map, we add it back to the heap and return a key from the map.
        while self.minHeap:
            val = heapq.heappop(self.minHeap)
            if self.count_key[val]:
                heapq.heappush(self.minHeap, val)
                for key in self.count_key[val]:
                    return key


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()


