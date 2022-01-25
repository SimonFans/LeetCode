Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
Example 1:
Input: "()"
Output: True
Example 2:
Input: "(*)"
Output: True
Example 3:
Input: "(*))"
Output: True


class Solution:
    def checkValidString(self, s: str) -> bool:
        '''
        li: smallest possible number of open left brackets
        hi: largest possible number of open left brackets
        '''
        li, hi = 0, 0
        for char in s:
            if char == '(':
                li += 1
            else:
                li -= 1
            if char != ')':
                hi += 1
            else:
                hi -= 1
            if hi < 0:
                break
            li = max(li, 0)
        return li == 0
        
