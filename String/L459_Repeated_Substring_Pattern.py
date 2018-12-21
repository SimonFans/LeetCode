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
