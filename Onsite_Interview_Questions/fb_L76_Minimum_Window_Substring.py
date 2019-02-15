Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.


class Solution(object):
    def minWindow(self, s, t):
        """
        双指针
        :type s: str
        :type t: str
        :rtype: str
        """
        total=len(t) # T中的长度
        cnt=dict()   #初始化S和T中都为0，之后T中的加1
        start=0      # 记录开始的位置
        mini=2000000 # set the default minimum length
        for i in s:
            cnt[i]=0
        for i in t:
            cnt[i]=cnt.get(i,0)+1
        j=0
        for i in range(len(s)):
            if cnt.get(s[i],0)>0:
                total-=1
            cnt[s[i]]=cnt.get(s[i],0)-1
            while total==0:
                if i-j+1<mini:
                    mini=i-j+1
                    start=j

                cnt[s[j]]=cnt.get(s[j],0)+1
                if cnt.get(s[j],0)>0:
                    total+=1
                j+=1

        return '' if mini==2000000 else s[start:start+mini]
    
