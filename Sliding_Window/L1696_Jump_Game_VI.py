'''
You are given a 0-indexed integer array nums and an integer k.

You are initially standing at index 0. In one move, you can jump at most k steps forward without going outside the boundaries of the array. That is, you can jump from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.

You want to reach the last index of the array (index n - 1). Your score is the sum of all nums[j] for each index j you visited in the array.

Return the maximum score you can get.
'''

Input: nums = [1,-1,-2,4,-7,3], k = 2
Output: 7
Explanation: You can choose your jumps forming the subsequence [1,-1,4,3] (underlined above). The sum is 7.
  
Input: nums = [10,-5,-2,4,0,3], k = 3
Output: 17
Explanation: You can choose your jumps forming the subsequence [10,4,3] (underlined above). The sum is 17.
  

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # nums = [1,-1,-2,4,-7,3], k = 2
        n = len(nums)
        score = nums[0]
        # (index, value)
        dq = deque()
        dq.append((0,score))
        
        for i in range(1, len(nums)):
            # 超出窗口大小，移走最左边的index, dp[0][0]起跳点
            while dq and dq[0][0] < i - k:
                dq.popleft()
            # 当没有超出窗口，计算起跳点的值+后面的值和之后用来比大小
            score = dq[0][1] + nums[i]
            # 如果当前加到的值大于之前的，则删掉之前的，永远将最大值放在首位，最后返回首位值，即为累加和的最大值
            while dq and score >= dq[-1][1]:
                dq.pop()
            dq.append((i,score))
        return score
