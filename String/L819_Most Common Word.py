Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.

 

Example:

Input: 
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.


from collections import defaultdict
import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        if not paragraph:
            return ""
        # return list, match word only
        strs=re.findall(r"\w+", paragraph.lower())
        exclude=set()
        for word in banned:
            exclude.add(word.lower())
        
        counts=defaultdict(int)
        maxCnt=0
        for i in range(len(strs)):
            strs[i]=strs[i].lower()
            if strs[i].isalnum() and strs[i] not in exclude:
                counts[strs[i]]+=1
                if counts[strs[i]]>maxCnt:
                    maxCnt=counts[strs[i]]
        res=[]
        for key,value in counts.items():
            if value==maxCnt:
                res.append(key)
        return "".join(res)
        
