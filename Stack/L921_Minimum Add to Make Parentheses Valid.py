'''
Given a string s of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:

It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.


Input: s = "())"
Output: 1

Input: s = "((("
Output: 3

Input: s = "()"
Output: 0

Input: s = "()))(("
Output: 4

Note:

s.length <= 1000
s only consists of '(' and ')' characters.
'''

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        stack = []
        ans = 0
        for symbol in s:
            if symbol == '(':
                stack.append(symbol)
                ans+=1
            else:
                if stack and stack[-1] == '(':
                    stack.pop()
                    ans -= 1 
                    continue
                elif stack and stack[-1] != '(':
                    stack.pop()
                    ans+=1
                else:
                    ans += 1
        return ans
   
