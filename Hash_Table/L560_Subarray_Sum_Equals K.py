Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2

#遍历到某个值的时候，可以看再加上这个值之前有多少组相加的值为k

class Solution:
    def subarraySum(self, nums: 'List[int]', k: 'int') -> 'int':
        ans=0  # return result
        sum=0  # do sum 
        d = collections.defaultdict(int)
        d[0]=1  # initial condition
        for i in range(len(nums)):
            sum+=nums[i]  # 前 n sum
            if sum-k in d:   # 前 n 项和-k 在字典里
                ans+=d[sum-k]   # 拿出之前加到这个数，有多少个给ans
            d[sum]+=1    # 每次把当前和记录当字典中
        return ans
