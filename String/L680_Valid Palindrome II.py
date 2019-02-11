Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.

class Solution:
    def validPalindrome(self, s: 'str') -> 'bool':
        left,right=0,len(s)-1
        while left < right:
            if s[left]!=s[right]:
                return self.isValidPalindrome(s,left,right-1) or self.isValidPalindrome(s,left+1,right)
            left+=1
            right-=1
        return True
    
    def isValidPalindrome(self,s,left,right):
        while left < right:
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True
