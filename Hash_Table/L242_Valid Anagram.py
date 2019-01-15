Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict1=dict()
        dict2=dict()
        for i in s:
            dict1[i]=dict1.get(i,0)+1
        for j in t:
            dict2[j]=dict2.get(j,0)+1
        return dict1==dict2
