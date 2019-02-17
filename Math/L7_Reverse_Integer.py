Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>0:
            n=x
        else:
            n=-x
        res=0
        while n:
            res=res*10+n%10
            n=n//10
        if res>2**31-1:
            return 0
        return res if x>0 else -res

    # Method 2:
    
    class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res=''
        if x>0:
            xstr=str(x)
        else:
            xstr=str(-x)
        l=len(xstr)-1
        while l>=0:
            res+=xstr[l]
            l-=1
        if int(res)>2**31-1:
            return 0
        return int(res) if x>0 else -int(res)
    
