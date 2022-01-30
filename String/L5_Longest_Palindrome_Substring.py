Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
    
    
# 中心扩散法，分奇偶情况,每次传基数长度之后偶数长度
# Time: O(n^2): Since expanding a palindrome around its center could take O(n) time, the overall complexity is O(n^2).
# Space: O(1) 


'''
Thoughts:
a palindrome mirrors around its center. Therefore, a palindrome can be expanded from its center.
If n is the length of the string, then there's only 2n - 1 such centers.
example:
s = 'abc'
so the center will be a, b, c, ab, and bc which is 2n-1 = 5
'''
    
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
        

            
