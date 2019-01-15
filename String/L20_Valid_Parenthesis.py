Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        mapping={")":"(","]":"[","}":"{"}
        for char in s:
            if char in mapping:
                if stack:
                    top=stack.pop()
                else:
                    top="#"
                if mapping[char]!=top:
                    return False
            else:
                stack.append(char)
        return not stack
        
