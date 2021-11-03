Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

Method(1)
    
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        d = {}
        start = -1
        longest_len = 0
        for i in range(len(s)):
            if s[i] in d and d[s[i]] > start:
                start = d[s[i]]
                d[s[i]] = i
            else:
                d[s[i]] = i
                longest_len = max(longest_len, i-start)
        return longest_len

# d[s[i]]>start? => start moves to first m when it finds the second m, 
# when second t finds, start position update only when first t position after start pointer
【example】
# t   m     m    z    u   x   t
#   start


Method (2)

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        list_=[]
        Lmax=0
        for i in s:
            if i in list_:
                del list_[0:list_.index(i)+1]
                list_.append(i)
            else:
                list_.append(i)
                if len(list_)>Lmax:
                    Lmax=len(list_)
        return Lmax

  // HashMap method   
  

