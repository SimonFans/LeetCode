"""
Input:  [1,2,3,4]

Output: [24,12,8,6]

ideas:
{1                       a[0]      a[0]*a[1]    a[0]*a[1]*a[2]  }
{a[1]*a[2]*a[3]       a[2]*a[3]       a[3]               1      }

O(N)
"""

class solution:
    def productExceptSelf(self, nums):
        length = len(nums)
        left = [0 for i in range(length)]
        right = [0 for i in range(length)]
        res = [0 for i in range(length)]
        left[0] = 1
        right[length-1] = 1
        for i in range(0, length-1):
            left[i+1] = left[i]*nums[i]
        for j in range(length-1,0,-1):
            right[j-1] = right[j]*nums[j]

        for k in range(length):
            res[k]=left[k]*right[k]
        return res

test = solution()
nums = [1, 2, 3, 4]
print(test.productExceptSelf(nums))
