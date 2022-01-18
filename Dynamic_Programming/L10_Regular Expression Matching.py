
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


# video: explain very well: https://www.youtube.com/watch?v=HAA8mgxlov8
'''
good example:
s = aab
p = c*a*b

top down memorization
two pointers. 
One points to current pos in string, the other one points to current pos in pattern.
'''
 
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def dfs(i,j):
            if (i,j) in cache:
                return cache[(i,j)]
            # If pointer i and j beyond the length of both s and p, then find the match
            if i>= len(s) and j >= len(p):
                return True
            # if pattern one has beyond the length of itself
            if j >= len(p):
                return False
            
            # guarantee the len of string is still inbound
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            # deal with '*' case. as we know, * cannot show at the beginning
            # (1) If we use *, then dfs(i+1,j)
            # (2) If we don't use *, then dfs(i, j+2)
            if j+1 < len(p) and p[j+1] == '*':
                # if use *, which means current pos matches, that's why do match and..
                cache[(i,j)] = (match and dfs(i+1,j)) or dfs(i, j+2)
                return cache[(i,j)]
            if match:
                cache[(i,j)] = dfs(i+1, j+1)
                return cache[(i,j)]
            cache[(i,j)] = False
            return False
        cache = {}
        return dfs(0,0)
            
            
    
