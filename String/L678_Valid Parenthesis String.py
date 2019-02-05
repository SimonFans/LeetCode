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
    def checkValidString(self, s: 'str') -> 'bool':
        lo = hi = 0
        for c in s:
            if c == '(':
                lo += 1 
            else:
                lo-=1
            if c != ')':
                hi += 1 
            else:
                hi-=1
            if hi < 0: break
            lo = max(lo, 0)
            
Time Complexity: O(N)O(N), where NN is the length of the string. We iterate through the string once.

Space Complexity: O(1)O(1), the space used by our lo and hi pointers. However, creating a new character array will take O(N)O(N) space.
