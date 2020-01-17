Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.

Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.


class Solution:
    def numSquares(self, n: int) -> int:
        cnt=0
        
        # case when n=1
        if n<2:
            return n
        
        # 存比n小的平方数，如1的平方是1，2的平方是2。。
        square_num=[]
        i=1
        while i*i<=n:
            square_num.append(i*i)
            i+=1
        # 被调查的数字
        checked_num=[n]
        
        # 可以理解x,y位被减数和减数的关系
        while checked_num:
            cnt+=1
            next_checked_num=set()
            for x in checked_num:
                for y in square_num:
                    if x==y:
                        return cnt
                    if x<y:
                        break
                    next_checked_num.add(x-y)
                checked_num=next_checked_num
        return cnt
                
                
 
