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
        res = 0
        str_len = len(s)
        if str_len == 0:
            return res
        stack = []
        dic = {')':'('}
        i = 0 
        while i < str_len:
            if s[i] == '(':
                stack.append(s[i])
            else:
                if not stack:
                    res += 1 
                elif stack[-1] == dic[s[i]]:
                    stack.pop()                    
            i += 1
        if len(stack) != 0:
            return len(stack) + res
        return res
   
