Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5

class Solution:
    def calculate(self, s: str) -> int:
        # record 之前的结果
        stack=[]
        # 记录之前数字
        num=0
        # pre_operator='+'
        pre_operator='+'
        for i, each in enumerate(s):
            if each.isdigit():
                num=10*num+int(each)
            if i==len(s)-1 or each in "+-*/":
                if pre_operator=='+':
                    stack.append(num)
                elif pre_operator=='-':
                    stack.append(-num)
                elif pre_operator=='*':
                    stack.append(stack.pop()*num)
                elif pre_operator=='/':
                    stack.append(int(stack.pop()/num))
                pre_operator=each
                num=0
        return sum(stack)
        
        
