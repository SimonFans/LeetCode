



'''
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Input: s = "3+2*2"
Output: 7

Input: s = " 3/2 "
Output: 1

Input: s = " 3+5 / 2 "
Output: 5
'''


class Solution:
    def calculate(self, s: str) -> int:
        #此题未涉及到小括号问题，但字符间可能存在空格

        stack = []
        current_number = 0
        res = 0
        operation = '+'
        
        for i in range(len(s)):
            current_char = s[i]
            if s[i].isdigit():
                current_number = current_number *10 + int(current_char)
            if not s[i].isdigit() and not s[i].isspace() or i == len(s) - 1:
                if operation == '+':
                    stack.append(current_number)
                elif operation == '-':
                    stack.append(-current_number)
                elif operation == '*':
                    previous_number = stack.pop()
                    stack.append(previous_number * current_number)
                elif operation == '/':
                    previous_number = stack.pop()
                    if previous_number * current_number < 0:
                        stack.append(-(abs(previous_number) // abs(current_number)))
                    else:
                        stack.append(previous_number // current_number)
                operation = current_char
                current_number = 0
        
        while stack:
            res += stack.pop()
        
        return res 
      
