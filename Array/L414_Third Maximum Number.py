Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.

#设一个最小值对三个初始变量，之后if语句判断

class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       
        mini=-sys.maxsize
        max1,max2,max3=mini,mini,mini
        for num in nums:
            if num>max1:
                max2,max3=max1,max2
                max1=num
            elif num>max2 and num<max1:
                max2,max3=num,max2
            elif num>max3 and num<max2:
                max3=num
           
        return max1 if max3==mini else max3
        
        
        
