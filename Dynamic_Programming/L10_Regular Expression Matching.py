
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.

Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

    
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".

    
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False for j in range(len(p) + 1)] for i in range(len(s) + 1)]
        #empty string with empty pattern
        dp[0][0] = True
        #handle the first row with empty string
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                #check if char in string match the pattern or pattern is '.'
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    #check condition without '*' and one char before
                    if dp[i][j - 2]:
                        dp[i][j] = True
                    #check condition with one or more char before '*'
                    elif s[i - 1] == p[j - 2] or p[j - 2] == '.':
                        dp[i][j] = dp[i - 1][j]
                else:
                    #not matching, keep dp[i][j] to False
                    continue

        return dp[len(s)][len(p)]
sol = Solution()
sol.isMatch('xaabyc', 'xa*b.c')
  
# if only match '.'  => see below solution
    
  class Solution:
    def isMatch(self, s: 'str', p: 'str') -> 'bool':
        dp=[[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        dp[0][0]=True
       
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1]=='.':
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=dp[i-1][j-1] and s[i-1]==p[j-1]
        return dp[len(s)][len(p)]

