Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S.

Example :
Input: 
S = "abcde"
words = ["a", "bb", "acd", "ace"]
Output: 3
Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".


from collections import defaultdict

class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        
        m=dict()
        
        def isMatch(word,d):
            if word in m:
                return m[word]
            prev=-1
            for w in word:
                index=bisect.bisect_left(d[w],prev+1)
                if index==len(d[w]):
                    return 0
                prev=d[w][index]
            m[word]=1
            return 1
            
        d=defaultdict(list)
        
        ans=0
        
        for i,s in enumerate(S):
            d[s].append(i)
        
        for word in words:
            ans+=isMatch(word,d)
        
        return ans
        
        
