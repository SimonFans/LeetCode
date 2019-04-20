Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
    
    
# 中心扩散法，分奇偶情况,每次传基数长度之后偶数长度
# O(n) O(1)
    
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def getPalindrome(s,left,right):
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
            return s[left+1:right]
            
        #(1) 判断字符串是否为空
        if not s:
            return ""
        
        #(2) define result as an empty string 
        longest=""
        for i in range(len(s)):
            odd_one=getPalindrome(s,i,i)
            if len(odd_one)>len(longest):
                longest=odd_one
            even_one=getPalindrome(s,i,i+1)
            if len(even_one)>len(longest):
                longest=even_one
        return longest
        

            
