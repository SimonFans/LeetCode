Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false



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
