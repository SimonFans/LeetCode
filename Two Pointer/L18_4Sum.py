Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums)<4:
            return []
        dic=dict()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                sum2=nums[i]+nums[j]
                if sum2 in dic:
                    dic[sum2].append((i,j))
                else:
                    dic[sum2]=[(i,j)]
        res=set()
        for key in dic:
            value=target-key
            if value in dic:
                list1=dic[key]
                list2=dic[value]
                for (a,b) in list1:
                    for (c,d) in list2:
                        if a!=c and a!=d and b!=c and b!=d:
                            temp=[nums[a],nums[b],nums[c],nums[d]]
                            temp.sort()
                            res.add(tuple(temp))
        return list(res)
        
