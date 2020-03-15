Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.

Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".

Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26

class Solution:
    def maxLength(self,arr):
	    lst, m = [""], 0
	    for s in arr:
		    for i in range(len(lst)):
			    t = s + lst[i]
			    l = len(t)
			    if l == len(set(t)):
				    lst.append(t)
				    m = max(m, l)
	    return m
      

# Solution 2: using DP https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/discuss/414172/PythonC%2B%2BJava-Set-Solution

def maxLength(self, A):
        dp = [set()]
        for a in A:
            if len(set(a)) < len(a): continue
            a = set(a)
            for c in dp[:]:
                if a & c: continue
                dp.append(a | c)
        return max(len(a) for a in dp)  
