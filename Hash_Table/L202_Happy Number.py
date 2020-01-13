Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
1^2+9^2=82


class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 如果出现循环，有两种情况，[1,1,1...] so yes, but if [18,...18] 18 is not 1, so no 
        
        c=set()
        while not n in c:
            c.add(n)
            n=sum([int(i)**2 for i in str(n)])
        return n==1
