Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        
        # [T,T,T,T,T,T,T,T,T,T]
        # [0 ................9] because not include 10, 从2开始，倍数乘积标为FALSE，最后统计TRUE的个数
        """
        if n<3:
            return 0
        res=[True]*n
        res[0]=res[1]=False
        for i in range(2,int(math.sqrt(n))+1):
            res[i*i:n:i]=[False]*len(res[i*i:n:i])
        return sum(res)
