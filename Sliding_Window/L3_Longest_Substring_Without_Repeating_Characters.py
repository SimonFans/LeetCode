'''
Given a string s, find the length of the longest substring without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
  
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
  
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0,0
        maxLen = 0
        hashMap = collections.defaultdict(int)
        while right < len(s):
            hashMap[s[right]] += 1
            while hashMap[s[right]] > 1:
                hashMap[s[left]] -= 1
                left += 1
            maxLen = max(maxLen, right-left+1)
            right += 1
        return maxLen
