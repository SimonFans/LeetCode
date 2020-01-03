Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Note: 
You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?


"""
dq: 存数组下标, 将窗口最大值下标放在首位

"""

import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 因为要用dq的popleft()方法
        dq=collections.deque()
        res=[]
        for i in range(len(nums)):
            # 只要前面的数比当前的数小，就去掉
            while dq and nums[dq[-1]]<=nums[i]:
                dq.pop()
            dq.append(i)
            # 保证窗口长度<=k, 大于k则去掉最左边的数
            if dq[0]==i-k:
                dq.popleft()
            # 当i遍历到大于等于k-1,将最左边的数压入结果list中去
            if i>=k-1:
                res.append(nums[dq[0]])
        return res
        
        
        
