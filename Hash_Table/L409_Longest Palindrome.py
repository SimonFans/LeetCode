Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        t=dict()
        res=0
        temp=0
        # count the number of characters
        for i in s:
            t[i]=t.get(i,0)+1
        # if even, add the value
        for x in t:
            if t[x]%2==0:
                res+=t[x]
        # if odd and count(odd)>1, add odd-1 and make dict-2
        for x in t:
            if t[x]%2==1 and t[x]>1:
                res+=t[x]-1
                t[x]-=2
        # if odd, only count 1
        for x in t:
            if t[x]%2==1:
                temp=1

        return res+temp
