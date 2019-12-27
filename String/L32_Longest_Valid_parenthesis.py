Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"

# start=-1 => 开头是（ ， （）
# (())


class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=0
        start=-1
        stack=[]
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            else:
                # if is ')', start pointer moves with i
                if len(stack)==0:
                    start=i
                else:
                    stack.pop()
                    if len(stack)==0:
                        res=max(res,i-start)
                    else:
                        res=max(res,i-stack[-1])
        return res
