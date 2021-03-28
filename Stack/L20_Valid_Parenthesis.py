'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Input: s = "()"
Output: true
  
Input: s = "()[]{}"
Output: true
  
Input: s = "(]"
Output: false

Input: s = "([)]"
Output: false

Input: s = "{[]}"
Output: true
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        # iterate string from left to right
        for char in s:
            # if meet a closing parenthesis
            if char in mapping:
                # if stack is empty then return false, otherwise stack pop to compare with current symbol
                if stack:
                    if mapping[char] == stack[-1]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            # if meet a openning parenthesis
            else:
                stack.append(char)
        return not stack
      
      
     
