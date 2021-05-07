'''
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Input: s = "aba"
Output: true
  
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'
  
Input: s = "abc"
Output: false
  
'''

class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                keep_left, keep_right = s[left:right], s[left + 1:right + 1]
                return keep_left == keep_left[::-1] or keep_right == keep_right[::-1]
            left, right = left + 1, right - 1
        return True 
  
  
