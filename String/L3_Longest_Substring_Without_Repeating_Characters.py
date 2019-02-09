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

  // HashMap method   
  
class Solution:
    def lengthOfLongestSubstring(self, s: 'str') -> 'int':
        n=len(s)
        ans=0
        Map_=dict()
        i=0
        for j in range(n):
            if s[j] in Map_:
                i=max(Map_.get(s[j]),i)
            ans=max(ans,j-i+1)
            Map_[s[j]]=j+1
            
        return ans
