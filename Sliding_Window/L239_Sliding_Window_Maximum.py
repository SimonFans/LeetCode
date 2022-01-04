'''
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
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
 '''

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Final return
        ans = []
        # queue stores all index
        queue = collections.deque()
        
        for curr_index, curr_val in enumerate(nums):
            # when queue is not empty and current value > the previous value
            while queue and curr_val > nums[queue[-1]]:
                queue.pop()
            queue.append(curr_index)
            # if current window length = k:
            if queue[0] + k == curr_index: 
                queue.popleft()
            # if and only if i step into k-1 position, it starts append the leftmost value, which is the maximum value
            if curr_index >= k-1:
                ans.append(nums[queue[0]])
        return ans
      
      
  
 
