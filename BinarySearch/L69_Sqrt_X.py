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
        
        if x < 2:
            return x
        
        left, right = 2, x//2
        # left <= right 终止条件一定是错位的left跑到right前面
        while left <= right:
            val = left + (right - left) // 2
            if val * val > x:
                right = val - 1
            elif val * val < x:
                left = val + 1
            else:
                return val
        
        return right
