Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=dict()
        res=[]
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=1
            else:
                d[nums[i]]=d.get(nums[i],0)+1
        sort_d=sorted(d.items(),key=lambda x: x[1], reverse=True)
        for j in range(k):
            res.append(sort_d[j][0])
        return res
        
        
