Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
The maximum number of consecutive 1s is 3.
    


class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt,ans=0,0
        for i in range(len(nums)):
            if nums[i]==1:
                cnt+=1
                ans=max(cnt,ans)
            else:
                cnt=0
        return ans
