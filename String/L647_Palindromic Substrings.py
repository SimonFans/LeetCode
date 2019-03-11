Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
 

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

class Solution:
    
    def countSubstrings(self, s: str) -> int:
        if len(s)==0:
            return 0
        size=len(s)
        res=0
        result=0
        for i in range(size):
            odd_nums=self.helper(s,i,i,res)
            even_nums=self.helper(s,i,i+1,res)
            result+=(odd_nums+even_nums)
        return result
    
    def helper(self, s, start, end, res):
        while start>=0 and end<len(s) and s[start]==s[end]:
            start-=1
            end+=1
            res+=1
        return res
       
