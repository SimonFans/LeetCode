Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

# 中心扩散法，o(n) o(1)

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s==None or len(s)==0:
            return s
        self.res=""
        for i in range(len(s)):
            self.helper(s,i,i)
            self.helper(s,i,i+1)
        return self.res
        
        
    def helper(self,s,left,right):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        cur=s[left+1:right]
        if len(cur) > len(self.res):
            self.res=cur
        return self.res        
