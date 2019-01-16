We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:
Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].

class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=0
        dict1=dict()
        for i in nums:
            dict1[i]=dict1.get(i,0)+1
        for i in dict1:
            if dict1.get(i,0)>0 and dict1.get(i+1,0)>0:
                if dict1.get(i,0)+dict1.get(i+1,0)>res:
                    res=dict1.get(i,0)+dict1.get(i+1,0)
        return res
