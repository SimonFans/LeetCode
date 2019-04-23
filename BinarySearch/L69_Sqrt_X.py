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
# If input n=8, finally left=3, right=2, so left>right overpass, result should return left-1.

class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x<2:
            return x
        
        left,right=1,x//2
        
        while left<=right:
            
            mid=left+(right-left)//2
            
            if mid**2>x:
                right=mid-1
            else:
                left=mid+1
                     
        return left-1   # when left>right 越界，取left-1. 
