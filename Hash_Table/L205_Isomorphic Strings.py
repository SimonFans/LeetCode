Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.

class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        # 解法2： return len(set(zip(s,t))) == len(set(s)) == len(set(t))
        # 用两个dict分别对应保存两个字符串对应位置的对方字符，只要其中一个不满足条件，则返回错误
        """
        if len(s)!=len(t):
            return False
        dict1=dict()
        dict2=dict()
        for i in range(len(s)):
            if (s[i] in dict1 and dict1[s[i]]!=t[i]) or (t[i] in dict2 and dict2[t[i]]!=s[i]):
                return False
            else:
                dict1[s[i]]=t[i]
                dict2[t[i]]=s[i]
        return True
    
