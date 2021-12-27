Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2

#遍历到某个值的时候，可以看再加上这个值之前有多少组相加的值为k

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash_table = collections.defaultdict(int)
        total = 0
        running_sum = 0
        for x in nums:
            running_sum += x
            _sum = running_sum - k
            if _sum in hash_table:
                total += hash_table[_sum]
            if running_sum == k:
                total += 1
            hash_table[running_sum] += 1
        return total
