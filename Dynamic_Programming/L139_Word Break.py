Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

# Method 1
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # DP, i从第二个字符开始+1，判断之前的组合（k从0开始到i）,如果有在list中，将当前i计TRUE
        
        d=[False for i in range(len(s)+1)]
        d[0]=True
        for i in range(1,len(s)+1):
            for k in range(i):
                if d[k] and s[k:i] in wordDict:
                    d[i]=True
        return d[len(s)]
        

# Method 2        
class Solution(object):
    def wordBreak(self,s,wordDict):
        
        queue=[0]  # 初始字符串下标
        ls=len(s)  # 字符串长度
        lenList=[l for l in set(map(len,wordDict))] # List中每段单词的长度
        visited = [0 for _ in range(0,ls+1)] # 记录访问到哪里了
        print("lenList",lenList)
        print("visited",visited)
        
        while queue:
            start=queue.pop(0)
            for l in lenList:
                if s[start:start+l] in wordDict:
                    if start+l==ls:
                        return True
                    if visited[start+l]==0:
                        queue.append(start+l)
                        visited[start+l]=1   
        return False

       
s="leetcode"
wordDict=["leet","code"]
print(Solution().wordBreak(s,wordDict))
        
