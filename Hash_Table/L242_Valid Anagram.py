Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dic=collections.defaultdict(int)
        for word1 in s:
            dic[word1]+=1
        for word2 in t:
            if word2 in dic:
                dic[word2]-=1
        for k, v in dic.items():
            if v!=0:
                return False
        return True
