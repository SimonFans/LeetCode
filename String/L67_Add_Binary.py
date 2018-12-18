Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        l1,l2=len(a)-1,len(b)-1
        flag=0
        res=''
        while l1>=0 and l2>=0:
            num=int(a[l1])+int(b[l2])+flag
            flag=num//2
            num%=2
            res=str(num)+res
            l1-=1;l2-=1
        while l1>=0:
            num=int(a[l1])+flag
            flag=num//2
            num%=2
            res=str(num)+res
            l1-=1
        while l2>=0:
            num=int(b[l2])+flag
            flag=num//2
            num%=2
            res=str(num)+res
            l2-=1
        if flag==1:
            res='1'+res
        return res
