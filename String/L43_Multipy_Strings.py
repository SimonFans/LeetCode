Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=="0" or num2=="0":
            return '0'
        
        # 取反，这样最右边的相乘数据在最左边，剩下的后面都是0，例：【72,109,119,0,0】
        num1=num1[::-1]
        num2=num2[::-1]

        arr=[0]*(len(num1)+len(num2))
        
        for i in range(len(num1)):
            for j in range(len(num2)):
                arr[i+j]+=int(num1[i])*int(num2[j])
        res=[]
        carry=0

        for k in range(len(arr)):
            number=(arr[k]+carry)%10
            res.append(str(number))
            carry=(arr[k]+carry)//10
        
        res=res[::-1]
        
        # consider case ['0',0','6'], need to remove leading zeros
        
        while res[0]=='0' and len(res)>1:
            del res[0]
            
        return ''.join(res)
