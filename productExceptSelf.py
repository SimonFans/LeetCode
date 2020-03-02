"""
Input:  [1,2,3,4]

Output: [24,12,8,6]

ideas:
{1                       a[0]      a[0]*a[1]    a[0]*a[1]*a[2]  }
{a[1]*a[2]*a[3]       a[2]*a[3]       a[3]               1      }

O(N)
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        length = len(nums)
        if length == 1:
            return 0
        result = [0 for i in range(length)]

        #from left to right
        #for first element, to make the value 1 now for easy multiply after
        result[0] = 1
        for i in range(1, length):
            result[i] = result[i-1] * nums[i-1]

        #from right to left
        #cause we cannot use the value already in the array to represent right to i+1
        #so we use a variable to keep the value
        right = 1
        for i in range(length - 1, -1, -1):
            result[i] *= right
            right *= nums[i]

        return result

test = solution()
nums = [1, 2, 3, 4]
print(test.productExceptSelf(nums))
