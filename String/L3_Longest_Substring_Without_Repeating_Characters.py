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
