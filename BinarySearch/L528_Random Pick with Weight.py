Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

Note:

1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.
Example 1:

Input: 
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]

Example 2:

Input: 
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array w. pickIndex has no arguments. Arguments are always wrapped with a list, even if there aren't any.


<直接看写的例子，此题例子给的不清楚>

"""
index: 0, 1, 2, 3
weight: 1, 8, 10, 2
prefixsum: 1, 9, 19, 21
[1]     [2,9]  [10, 19] [20, 21]
index=0 index=1 index=2 index=3
二分法解题

"""

import random

class Solution:

    def __init__(self, w: List[int]):
        # 初始化累加和数组，并求累加和
        self.prefixSum=[0]*len(w)
        self.prefixSum[0]=w[0]
        for i in range(1,len(w)):
            self.prefixSum[i]=self.prefixSum[i-1]+w[i]
        

    def pickIndex(self) -> int:
        if len(self.prefixSum) == 0:
            return 0
        target = random.randint(1, self.prefixSum[-1])
        start, end = 0, len(self.prefixSum)
        while start + 1 < end:
            
            mid = (start + end)//2
            if self.prefixSum[mid] < target:
                start = mid
            elif self.prefixSum[mid] > target:
                end = mid
            else:
                return mid
        if self.prefixSum[start] >= target:
            return start
        else:
            return end

            
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
