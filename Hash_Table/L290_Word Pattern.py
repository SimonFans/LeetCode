Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.

# 长度比较和set结合
class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        
        return len(pattern)==len(str.split(' ')) and len(set(zip(pattern,str.split(' '))))==len(set(pattern))==len(set(str.split(' ')))

    
    # 双字典同时存储
    class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        
        target=str.split(' ')
        
        if len(pattern)!=len(target):
            return False
        
        dict1=dict()
        dict2=dict()
        
        for i in range(len(pattern)):
            if (pattern[i] in dict1 and dict1[pattern[i]]!=target[i]) or (target[i] in dict2 and dict2[target[i]]!=pattern[i]) :
                return False
            else:
                dict1[pattern[i]]=target[i]
                dict2[target[i]]=pattern[i]
        return True
