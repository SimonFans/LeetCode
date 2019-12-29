Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.

 

Example 1:

Input: A = [4,5,0,-2,-3,1], K = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by K = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
 

Note:

1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000


import collections
"""
思路：

累加和求余，任意从相同的余数中选取两个，例如有4个余数为4的，则C42=6，代表有6个subarray可以被K整除

"""


class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        p=[0]
        dic=collections.defaultdict(int)
        ans=0
        # Get remainder list of sum aggregation
        for num in A:
            p.append((p[-1]+num)%K)
        # Count remainder
        for i in p:
            dic[i]+=1
        for v in dic.values():
            ans+=v*(v-1)//2
        return ans
        
        
        
