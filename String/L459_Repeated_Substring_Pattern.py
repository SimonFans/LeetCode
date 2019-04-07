Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

 

Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.
Example 2:

Input: "aba"
Output: False
Example 3:

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

 # 原理是，先提取字符串的一半，然后乘以2，看生成串和原串是否相同，相同则true，否则提取字符串三分之一，然后乘以3，以此类推
 class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if not str and len(str)<2:
            return False
        
        str_len=len(s)
        pos=str_len //2
        
        while pos>0:
            if str_len % pos ==0:
                substr=s[:pos]
                divisor=str_len // pos
                if substr * divisor == s:
                    return True
            pos-=1
        return False
 
 
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False

        ss = (s + s)[1:-1]
        return ss.find(s) != -


# 这个思想的精髓就在于通过拷贝一次字符串，并且各自破坏一小部分，然后通过两个串的拼接完成原串的查找。如果串不满足要求的特性，是拼装不出来的。
