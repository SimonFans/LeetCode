Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.


class Solution:
    def addStrings(self, num1: 'str', num2: 'str') -> 'str':
        result=[]
        carry=0
        l1,l2=len(num1),len(num2)
        while l1 or l2 or carry:
            digits=carry
            if l1:
                l1-=1
                digits+=int(num1[l1])
            if l2:
                l2-=1
                digits+=int(num2[l2])
            carry=digits>9
            result.append(str(digits%10))
        return ''.join(result[::-1])
            
                
        
