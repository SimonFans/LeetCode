Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.

# first string like 'abcd', second one is 'abc', then abc else get first string

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        
        for i in range(len(strs[0])):
            for string in strs[1:]:
                if i>=len(string) or strs[0][i]!=string[i]:
                    return strs[0][:i]
                
        return strs[0]
        
        
