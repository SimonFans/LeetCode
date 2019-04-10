Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to the multiple of k, that is, sums up to n*k where n is also an integer.

Example 1:

Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.

Example 2:

Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
 

Note:

The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.


"""
遍历数组nums，求前i项和total；对k取模，记模值为m

利用dmap[m]记录模为m的前i项和的最小下标，初始令dmap[0] = -1

若dmap[m] + 1 < i，则返回True


"""


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d={0:-1}
        total=0
        for i,n in enumerate(nums):
            total+=n
            m=total%k if k else total
            if m not in d:
                d[m]=i
            elif d[m]+1<i:
                return True
        return False
        
        
