Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=0  # 累积当前位之前的运算结果
        sign=1 # positive:1 negative:-1
        num=0  # computer only numbers
        stack=[]
        for c in s:
            if c.isdigit():
                num=10*num+int(c)
            elif c=='+' or c=='-':
                res=res+sign*num
                num=0
                sign=1 if c=='+' else -1
            elif c=='(':
                stack.append(res)
                stack.append(sign)
                res=0
                sign=1
            elif c==')':
                res=res+sign*num
                num=0
                res*=stack.pop()
                res+=stack.pop()
        res=res+sign*num
        return res
                
        
