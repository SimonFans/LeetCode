Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        low,high=0,num
        while low<=high:
            mid=low+(high-low)//2
            if mid**2==num:
                return True
            elif mid**2>num:
                high=mid-1
            else:
                low=mid+1
        return False
