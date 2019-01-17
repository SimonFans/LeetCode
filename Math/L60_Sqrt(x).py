Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
             
             
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<=0:
            return 0
        if x==1:
            return 1
        
        l,r=0,x//2
        while l<=r:
            mid=l+(r-l)//2
            if mid*mid == x:
                return int(mid)
            elif mid*mid<x:
                l=mid+1
            else:
                r=mid-1
        return int(r)
