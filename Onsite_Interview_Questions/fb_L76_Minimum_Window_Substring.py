Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.


from collections import defaultdict



class Solution():
    def minWindow(self,s,t):
        cnt=defaultdict(int)
        t_length=len(t)
        min_val=200000
        # 记录j的位置
        start=0
        
        for i in s:
            cnt[i]=0
        for i in t:
            cnt[i]+=1
        
        # 起始位置，之后会变动
        j=0
        for i in range(len(s)):
            if cnt[s[i]]>0:
                t_length-=1
            cnt[s[i]]-=1
            
            while t_length==0:
                if i-j+1<min_val:
                    min_val=i-j+1
                    start=j
                cnt[s[j]]+=1
                if cnt[s[j]]>0:
                    t_length+=1
                j+=1   
        return '' if min_val==200000 else s[start:start+min_val]
