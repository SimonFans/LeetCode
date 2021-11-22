'''
Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"

Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.

Example 4:

Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"
'''
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        index_to_remove = set()
        stack = []
        for index, char in enumerate(s):
            # all met chars except for "()"
            if char not in '()':
                continue
            # met "(" 
            elif char == '(':
                stack.append(index)
            # met ")" and stack is empty
            elif not stack:
                index_to_remove.add(index)
            else:
                stack.pop()
        # Find out all index that going to be removed from the string
        # After the above for loop, if stack still not empty then means more "(" left
        index_to_remove = index_to_remove.union(set(stack))
        res = []
        for i, char in enumerate(s):
            if i not in index_to_remove:
                res.append(char)
        return ''.join(res)
