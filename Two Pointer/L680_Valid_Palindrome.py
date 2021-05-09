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

# Solution 1:

class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                keep_left, keep_right = s[left:right], s[left + 1:right + 1]
                return keep_left == keep_left[::-1] or keep_right == keep_right[::-1]
            left, right = left + 1, right - 1
        return True 
  
# Solution 2:
  
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s, i, j):
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                cut_left = isPalindrome(s[left+1:right+1], left+1, right)
                cut_right = isPalindrome(s[left:right], left, right-1)
                return cut_left or cut_right
            left += 1
            right -= 1
        return True
      
      
