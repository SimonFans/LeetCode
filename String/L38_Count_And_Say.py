The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        i=1
        res="1"
        while i<n:
            count=0
            sb=""
            c=res[0]
            for j in range(len(res)+1):
                if j!=len(res) and res[j]==c:
                    count+=1
                else:
                    sb+=str(count)
                    sb+=c
                    if j!=len(res):
                        count=1
                        c=res[j]
            res=sb
            i+=1
        return res
