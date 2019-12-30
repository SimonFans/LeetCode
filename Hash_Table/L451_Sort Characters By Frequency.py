Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

Solution1: 
    
class Solution:
    def frequencySort(self, s: str) -> str:
        freq = collections.defaultdict(int)
        result=""
        
        for c in s:
            freq[c] += 1
            
        sort_freq=sorted(freq.items(),key=lambda x:x[1],reverse=True)
        for i in range(len(sort_freq)):
            if sort_freq[i][1]!=0:
                result += sort_freq[i][0]*sort_freq[i][1]
        return result

    
Solution2:
 
import collections

class Solution:
    def frequencySort(self, s: str) -> str:
        if s=="":
            return ""
        d=collections.defaultdict(int)
        temp=[]
        res=""
        for c in s:
            d[c]+=1
        for k,v in d.items():
            temp.append((v,k))
        temp.sort(key=lambda x:x[0],reverse=True)
        
        for l in temp:
            res+=l[0]*l[1]
        
        return res
