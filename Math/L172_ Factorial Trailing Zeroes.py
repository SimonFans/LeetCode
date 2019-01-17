Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity.

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        5!=1*2*3*4*5          1 ge 5
        10!=1*2 *...*5* 10    2 ge 5  
        转化成计算有多少个5 
        """ 
        
        res=0
        while n:
            n=n//5
            res+=n
        return res
        
        
