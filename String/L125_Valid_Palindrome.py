Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left,right=0,len(s)-1
        while left<right:
            while left<right and not s[left].isalnum():
                left+=1
            while left < right and not s[right].isalnum():
                right-=1
            if s[left].lower()!=s[right].lower():
                return False
            left+=1
            right-=1
        return True

    
    class Solution:
    def isPalindrome(self, s: 'str') -> 'bool':
        left,right=0,len(s)-1
        while left < right:
            if not s[left].isalnum():
                left+=1
                continue
            if not s[right].isalnum():
                right-=1
                continue
            if s[left].lower()==s[right].lower():
                left+=1
                right-=1
                continue
            return False    
        return True
