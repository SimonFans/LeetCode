Find the length of the longest substring T of a given string (consists of lowercase letters only) 
such that every character in T appears no less than k times.

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.



class solution():

    def longest_Substring_K(self,s,k):
        if k==0 or s is None or len(s)==0:
            return 0
        if len(s)<k:
            return len(s)
        maxLen=k
        start=0
        charmap=dict()
        print(type(charmap))
        for i in range(len(s)):
            c=s[i]
            if c not in charmap:
                charmap[c]=1
            else:
                charmap[c]+=1
            if len(charmap)>k:
                maxLen=max(maxLen,i-start)
                while len(charmap)>k:
                    fc=s[start]
                    if charmap[fc]>1:
                        charmap[fc]-=1
                    else:
                        del charmap[fc]
                    start+=1
        maxLen=max(maxLen,len(s)-start)
        #print(s[start:len(s)+1])
        return maxLen


test=solution()
s="abcadcacacaca"
k=3
print(test.longest_Substring_K(s,k))
