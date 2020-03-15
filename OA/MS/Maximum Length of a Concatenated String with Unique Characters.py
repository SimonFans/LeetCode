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
      
      
