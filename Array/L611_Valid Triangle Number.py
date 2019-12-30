Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

Example 1:
Input: [2,2,3,4]
Output: 3

Explanation:
Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3

Note:
The length of the given array won't exceed 1000.
The integers in the given array are in the range of [0, 1000].

"""
思路：

9 8 7 6 5 4 3 2 
c b           a

(1) 先做降序排列
(2) while b<a: 
        if c>a+b
            res+=(a-b)  // 如果cba可以，证明c 和b a 之间的都可以
            b+=1
        else:
            a-=1

"""

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        res=0
        for c in range(len(nums)-2):
            b,a=c+1,len(nums)-1
            while a>b:
                if nums[a]+nums[b]>nums[c]:
                    res+=a-b
                    b+=1
                else:
                    a-=1
        return res
