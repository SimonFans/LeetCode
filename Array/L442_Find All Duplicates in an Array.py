Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]


"""
遍历nums，记当前数字为n（取绝对值），将数字n视为下标（因为a[i]∈[1, n]）

当n首次出现时，nums[n - 1]乘以-1

当n再次出现时，则nums[n - 1]一定＜0，将n加入答案

"""

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans=[]
        for n in nums:
            if nums[abs(n)-1]<0:
                ans.append(abs(n))
            else:
                nums[abs(n)-1]*=-1
        return ans
        
        
        
