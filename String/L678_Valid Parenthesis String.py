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
        # left: 遇左括号和星号都加1，如果Left为0，则either没星号或者星号当作左括号与右边匹配
        left,right=0,0
        size=len(s)
        for i in range(size):
            if s[i]=='(' or s[i]=='*':
                left+=1
            else:
                left-=1
            if left<0:
                return False
        if left==0:
            return True
        # right: 遇右括号和星号都加1，如果right为0，* match右括号, 如果right大于0，星号可为空
        for i in range(size-1,-1,-1):
            if s[i]==')' or s[i]=='*':
                right+=1
            else:
                right-=1
            if right<0:
                return False
        return True
        
