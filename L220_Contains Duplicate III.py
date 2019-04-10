Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        a = set()
        for i in range(len(nums)):
            if t==0:
                if nums[i] in a:
                    return True
            else:
                for item in a:
                    if abs(nums[i]-item)<=t:
                        return True
            a.add(nums[i])
            if len(a) == k+1:
                a.remove(nums[i-k])
        return False


