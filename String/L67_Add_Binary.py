Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        '''
        Input: a = "1010", b = "1011"
        Output: "10101"
        '''
        n = max(len(a), len(b))
        # zfill 目的是将两个字符串等长，少的那个前面补0形成长度为n的字符串
        a, b = a.zfill(n), b.zfill(n)
        # result list
        ans = []
        # 进位为0
        carry = 0
        # 从后向前遍历，最后的时候记得要反向输出
        for i in range(n-1,-1,-1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1
            if carry % 2 == 1:
                ans.append('1')
            else:
                ans.append('0')
            # 此处无非是carry = 0,1,2,3
            carry //= 2
        
        if carry == 1:
            ans.append('1')
        ans.reverse()
        return ''.join(ans)
